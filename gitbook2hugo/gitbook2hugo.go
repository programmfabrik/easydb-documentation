package main

import (
	"flag"
	"fmt"
	"io"
	"bufio"
	"net/url"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"html"
	log "github.com/sirupsen/logrus"
	// "errors"
	"regexp"

	"gitbook2hugo/mark"
)


type LinkNode struct {
	mark.LinkNode
	Path string
}

var linkNodes []LinkNode
var linksFollowed map[string]bool
var images map[string]bool

func main() {
	path := flag.String("path", "./gb", "Path to gitbook")
	dumpfn := flag.String("dump", "", "File to dump")
	htmlfn := flag.String("html", "", "File to html")
	clean := flag.Bool("clean", false, "Remove content folder")
	quite := flag.Bool("quite", false, "Quite output")
	debug := flag.Bool("debug", false, "Set log  debug level")
	linksfn := flag.String("links", "", "Collect links")
	content := flag.String("content", "", "Create content folder")
	lang := flag.String("lang","","Add language parameter to index files")
	linkpre := flag.String("linkpre","","Add link prefix")

	flag.Parse()

	log.SetOutput(os.Stdout)

	if *debug {
		log.SetLevel(log.DebugLevel)
	}


	if *linksfn != "" {
		linksFollowed = make(map[string]bool, 100)
		linkNodes = make([]LinkNode, 100)
		images = make(map[string]bool, 100)

		menuByPath := make(map[string]string, len(linkNodes))

		FindLinks(*linksfn, "", false, *quite)
		for _, linkNode := range linkNodes {
			if len(linkNode.Nodes) == 0 {
				// fmt.Printf("Link Node with no nodes: %v", linkNode)
				continue
			}
			switch linkNode.Nodes[0].(type) {
			case *mark.TextNode:
				menuByPath[linkNode.Path] = html.UnescapeString((linkNode.Nodes[0].(*mark.TextNode)).Text)
			}
		}

		linksFollowed = make(map[string]bool, 100)
		linkNodes = make([]LinkNode, 100)

		FindLinks(*linksfn, "", true, *quite)

		// fmt.Printf("menu: %#v", menuByPath)

		// fmt.Printf("images: %#v", images)

		if *content == "" {
			for _, linkNode := range linkNodes {
				if len(linkNode.Nodes) > 0 {
					switch linkNode.Nodes[0].(type) {
					case *mark.TextNode:
						textNode := linkNode.Nodes[0].(*mark.TextNode)
						log.Debugf("%s - %s - %s", html.UnescapeString(textNode.Text), linkNode.Href, linkNode.Path)
					}
				}
			}
		} else {
			var files []string
			for fn, _ := range linksFollowed {
				files = append(files, fn)
			}
			sort.Strings(files)
			// path := *linksfn
			if *clean {
				log.Infof("Removing %s", *content)
				err := os.RemoveAll(*content)
				if err != nil {
					panic(err)
				}
			}

			for file_i, file := range files {
				rfile, err := os.Open(file)
				if err != nil {
					panic(err)
				}

				// remove linksfn from file (SUMMARY.md)
				cut_path := filepath.Dir(*linksfn)
				rel_path := file[len(cut_path)+1:]
				// target_top := filepath.Base(*content)

				filename := filepath.Base(rel_path)
				basename := strings.TrimSuffix(filename, filepath.Ext(filename))
				rel_path_dir := filepath.Dir(rel_path)
				source_dir := filepath.Dir(file)

				var targetFn string
				var targetDir string
				var name string

				targetDir = filepath.Clean(*content + "/" + rel_path_dir)

				multiple := false

				if rel_path_dir != "." {
					// fmt.Printf("%s == %s ?? %s\n", filepath.Base(rel_path_dir), basename, rel_path)
					// if filepath.Base(rel_path_dir) == basename {
					// if we have more than one ".md" file in the path,
					// we cannot use a hugo bundle
					m, err := filepath.Glob(source_dir+"/*.md")
					if err != nil {
						panic(err)
					}
					if len(m) == 1 {
						name = "_index"
					} else {
						log.Warnf("Multiple .md files in path: %s, not creating a bundle for %s %v.", source_dir, basename, m)
						name = basename
						multiple = true
					}
				} else {
					name = basename
				}

				if *lang != "" {
					targetFn = targetDir + "/"+name+"."+*lang+".md"
				} else {
					targetFn = targetDir + "/"+name+".md"
				}

				// fmt.Printf("%s rel: %s target: %s \n", *linksfn, rel_path, filepath.Dir(rel_path)) // targetFn)
				err = os.MkdirAll(targetDir, 0755)
				if err != nil {
					panic(err)
				}

				log.Debugf("%s -> %s", file, targetFn)

				_, err = os.Stat(targetFn)

				if err == nil {
					// fmt.Printf("%v", info, err)
					// panic(errors.New("File already exists in destination:"+targetFn))
				}

				wfile, err := os.Create(targetFn)
				if err != nil {
					panic(err)
				}
				var title string // filepath.Base(file)
				var ok bool
				var identifier string

				if title, ok = menuByPath[file]; !ok {
					title = file
				}
				// current := filepath.Base(targetDir)

				if multiple {
					identifier = strings.TrimSuffix(rel_path, filepath.Ext(rel_path))
				} else {
					identifier = rel_path_dir
				}

				parent := filepath.Dir(rel_path_dir)


				// write front matter
				fmt.Fprintf(wfile, "---\n")
				fmt.Fprintf(wfile, "title: \"%d - %s\"\n", file_i, title)
				if identifier == "/" || identifier == "." {
					fmt.Fprintf(wfile, "menu: \"%s\"\n", "main")
					// fmt.Printf("Menu: %s\n", "main")
				} else {
					fmt.Fprintf(wfile, "menu:\n")
					fmt.Fprintf(wfile, "  main:\n")
					fmt.Fprintf(wfile, "    name: \"%s\"\n", title)
					fmt.Fprintf(wfile, "    identifier: \"%s\"\n", identifier)
					if parent != "/" && parent != "." {
						fmt.Fprintf(wfile, "    parent: \"%s\"\n", parent)
					}
					log.Debugf("Title: %s Identifier: %s Parent: %s", title, identifier, parent)
				}
				fmt.Fprintf(wfile, "---\n")

				re := regexp.MustCompile(`\[(.+?)\]\((.+?)\)`)

				repl := func(str string) string {
					m := re.FindStringSubmatch(str)
					url, _ := url.Parse(m[2])
					if err != nil {
						return str
					}
					if url.Host != "" && url.Host != "docs.easydb.de" {
						return str
					}
					if strings.HasSuffix(url.Path, ".html") || strings.HasSuffix(url.Path, ".md") {
						// fmt.Printf("%s::: %s %s: !!\n", str, url.Host, url.Path) // , url.Path)
						var p string
						if url.Host != "" {
							p = url.Scheme + "://" + url.Host+ filepath.Dir(url.Path)
						} else {
							p = filepath.Dir(url.Path)

							if strings.HasPrefix(url.Path, "/") && *lang != "" {
								p = "/" + *lang + p
							}

							if strings.HasPrefix(url.Path, "/") && *linkpre != "" {
								p = "/" + *linkpre + p
							}
						}

						if m[1] != "" {
							return "["+m[1]+"]("+p+")"
						} else {
							return "("+p+")"
						}
					}
					return str
				}

				reImg := regexp.MustCompile(`\!\[(.+?)\]\((.+?)\)`)

				replImg := func(str string) string {
					// log.Warnf("Match: %s ", str)

					if *lang == "" {
						return str
					}

					m := re.FindStringSubmatch(str)

					filename := filepath.Base(m[2])
					ext := filepath.Ext(filename)
					basename := strings.TrimSuffix(filename, ext)

					if ext != ".png" {
						return str
					}

					var p string

					if filepath.Dir(filename) == "." {
						p = basename+"_" + *lang + ext
					} else {
						p = filepath.Dir(filename)+"/"+basename+"_" + *lang + ext
					}


					var new_p string
					if m[1] != "" {
						new_p = "!["+m[1]+"]("+p+")"
					} else {
						new_p = "!("+p+")"
					}
					log.Debugf("Image Link change: %s", new_p)
					return new_p
				}


				scanner := bufio.NewScanner(rfile)
				for scanner.Scan() {
					str := scanner.Text()
					str = re.ReplaceAllStringFunc(str, repl)
					str = reImg.ReplaceAllStringFunc(str, replImg)
					str = strings.Replace(str, "|--|", "|---|", -1)
					// if len(info) > 0 {
					// 	fmt.Println(info)
					// }
					_, err := wfile.WriteString(str+"\n")
					if err != nil {
						panic(err)
					}
				}

				rfile.Close()
				wfile.Close()

				// bytes, err := io.Copy(wfile, rfile)
				// if err != nil {
				// 	panic(err)
				// }

				// _ = bytes

			}


			for imagefn, _ := range images {
				rfile, err := os.Open(imagefn)
				if err != nil {
					log.Errorf("Error copying image: %s", err)
					continue
				}

				// remove linksfn from file (SUMMARY.md)
				cut_path := filepath.Dir(*linksfn)
				rel_path := imagefn[len(cut_path)+1:]
				// target_top := filepath.Base(*content)


				filename := filepath.Base(rel_path)
				ext := filepath.Ext(filename)
				basename := strings.TrimSuffix(filename, ext)
				rel_path_dir := filepath.Dir(rel_path)

				var targetDir string
				var targetFn string

				targetDir = filepath.Clean(*content + "/" + rel_path_dir)

				if *lang == "" {
					targetFn = targetDir + "/" + filename
				} else {
					targetFn = targetDir + "/" + basename + "_" + *lang + ext
				}

				if _, err := os.Stat(targetFn); !os.IsNotExist(err) {
					log.Errorf("Image already exists in destination: %s. Not copying.", targetFn)
					continue
				}

				log.Debugf("COPY: %s rel: %s target: %s", imagefn, rel_path, targetFn)

				err = os.MkdirAll(targetDir, 0755)
				if err != nil {
					panic(err)
				}

				wfile, err := os.Create(targetFn)
				if err != nil {
					panic(err)
				}
				_, err = io.Copy(wfile, rfile)
				if err != nil {
					panic(err)
				}

				rfile.Close()
				wfile.Close()
			}

		}
	} else if *htmlfn != "" {
		fmt.Print(mark.RenderFile(*htmlfn))
	} else if *dumpfn != "" {
		mark.DumpFile(*dumpfn)
	} else {

		fmt.Printf("Path: %s\n", *path)

		mark.DumpFile(*path + "/LANGS.md")
		mark.DumpFile(*path + "/de/SUMMARY.md")
		mark.DumpFile(*path + "/en/SUMMARY.md")
	}
}

func FindLinks(fn string, rootpath string, dive bool, quite bool) {
	if _, ok := linksFollowed[fn]; ok {
		return
	}

	p := mark.ParseFile(fn)
	space := " " // strings.Repeat("   ", level)

	linksFollowed[fn] = true

	line := strings.Repeat("-", len(fn))

	if !quite {
		fmt.Printf("%s\n%s\n%s\n", line, fn, line)
	}

	path := filepath.Dir(fn)

	if rootpath == "" {
		rootpath = path
	}

	moreLinks := make([]string, 0, 10)

	for _, node := range p.Nodes {
		// fmt.Printf("%sNode: %s\n\n", space, node.NodeName())
		nodes := mark.CollectNode(node, func(node mark.Node) bool {
			// fmt.Printf("%Node: %s\n", node.NodeName())
			switch node.(type) {
			case *mark.ImageNode:
				return true
			case *mark.LinkNode:
				return true
			default:
				return false
			}
		})

		for _, node := range nodes {
			switch node.(type) {
			case *mark.ImageNode:
				imageNode := node.(*mark.ImageNode)
				// if !quite {
				// }
				// fmt.Printf("%sIMG: %s\n", space, node.NodeName())

				if strings.HasPrefix(imageNode.Src, "/") {
					images[filepath.Clean("gb/"+imageNode.Src)] = true
				} else {
					images[path+"/"+imageNode.Src] = true
				}

			case *mark.LinkNode:
				linkNode := node.(*mark.LinkNode)
				localLinkNode := LinkNode{*linkNode, ""}

				fn2 := ""

				url, err := url.Parse(linkNode.Href)
				if err != nil {
					if !quite {
						log.Warnf("%sLINK: **broken** '%s'**\n", space, node.NodeName())
					}
					continue
				}

				if strings.HasPrefix(linkNode.Href, "#") {
					if !quite {
						log.Debugf("%sLINK: %s\n", space, linkNode.Href)
					}
					continue
				}

				if url.Scheme != "" {
					if !quite {
						log.Debugf("%sEXT: %s\n", space, linkNode.Href)
					}
					continue
				}

				if strings.HasSuffix(url.Path, ".md") {
					// Follow this
					fn2 = url.Path
				}

				if strings.HasSuffix(url.Path, ".html") {
					fn2 = strings.Replace(url.Path, ".html", ".md", -1)
				}

				if fn2 == "" {
					if !quite {
						log.Warnf("%sLINK: **unknown** %s\n", space, linkNode.Href)
					}
					continue
				}

				var fn3 string
				if strings.HasPrefix(fn2, "/") {
					fn3 = rootpath + fn2
				} else {
					fn3 = path + "/" + fn2
				}

				fn3 = filepath.Clean(fn3)

				if fileInfo, err := os.Stat(fn3); err != nil || fileInfo.IsDir() {
					if !quite {
						fmt.Printf("%sLINK: **broken** '%s'**\n", space, linkNode.Href)
					}
					// fmt.Printf("%s P:%s\n", space, path)
					// fmt.Printf("%sFN:%s\n", space, fn3)
					continue
				}

				if !quite {
					log.Debugf("%sLINK: %s\n", space, fn3)
				}

				localLinkNode.Path = fn3
				linkNodes = append(linkNodes, localLinkNode)

				moreLinks = append(moreLinks, fn3)
			}
		}
	}
	// fmt.Printf("LINKs: %v", moreLinks)

	if dive {
		for _, link1 := range moreLinks {
			FindLinks(link1, rootpath, dive, quite)
		}
	}
}
