/*

Folder fold/unfold
==================

*/

(function() {

	var diagramEntries = document.querySelectorAll("code.language-sequence")
	for(var i = 0; i < diagramEntries.length; i++){
		var diagramEntry = diagramEntries[i]
		var diagram = Diagram.parse(diagramEntry.textContent);
		diagramEntry.innerHTML = ""
		diagram.drawSVG(diagramEntry, {theme: "hand"})
	}

	var open_menus = JSON.parse(window.localStorage.getItem("easydb-docs-open-menus") || '[]');
	// console.debug("open menus:", open_menus)

	var menuEntries = document.querySelectorAll('.js-toggle-menu')

	for(var i = 0; i < menuEntries.length; i++){
		var menuEntry = menuEntries[i]
		var li = menuEntry.parentNode.parentNode
		var menu = li.getAttribute("menu-identifier")
		var idx = open_menus.indexOf(menu)

		// console.debug(menuEntry, menu, idx)
		if (idx > -1) {
			do {
				if (li.classList.contains("menu-entry")) {
					li.classList.add("is-open")
				}
				break
				li = li.parentNode
			} while (li != document.body)
		}

		menuEntry.addEventListener('click', onMenuToggleClick)
	}

	var currentMenuEntry = document.querySelectorAll('.menu-entry.current')
	if (currentMenuEntry.length > 0) {
		CUI.dom.scrollIntoView(currentMenuEntry[0])
	}


	function onMenuToggleClick(event){
		event.preventDefault()
		var li = event.target.parentNode.parentNode
		li.classList.toggle("is-open")
		var menu = li.getAttribute("menu-identifier")
		var idx = open_menus.indexOf(menu)
		if (li.classList.contains("is-open")) {
			if (idx == -1) {
				open_menus.push(menu)
			}
		} else {
			if (idx > -1) {
				open_menus.splice(idx, 1)
			}
		}

		window.localStorage.setItem("easydb-docs-open-menus", JSON.stringify(open_menus));
	}
})()


/*

Save Menu scroll-position
=========================

*/


var menu = document.querySelector('.js-menu');
var scrollPosition = parseInt(sessionStorage.getItem('menu-scroll'), 10);

if(scrollPosition){
	menu.scrollTop = scrollPosition;
}

menu.classList.add('is-loaded');
menu.addEventListener('scroll', saveScrollPosition);

function saveScrollPosition(){
	sessionStorage.setItem('menu-scroll', menu.scrollTop);
}






/*

Fullscreen Image Popover
========================

*/

var images = document.querySelectorAll('main img');

for(var i=0; i<images.length; i++){
	images[i].addEventListener('click', onImageClick);
}

function onImageClick(){
	var popover = document.createElement('div');
	popover.classList.add("popover");
	var image = new Image();
	image.classList.add("popover-image");
	image.src = this.src;
	popover.appendChild(image);
	popover.addEventListener("click", function(){ this.remove(); });
	document.body.appendChild(popover);
}
