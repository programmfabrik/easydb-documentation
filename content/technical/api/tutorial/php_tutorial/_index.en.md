---
title: "80 - PHP"
menu:
  main:
    name: "PHP"
    identifier: "technical/api/tutorial/php_tutorial"
    parent: "technical/api/tutorial"
---
# PHP Quickstart 
    Use PHP with Xampp or Javascript JQuery

## Table of Contents

---

 - [Getting Started](#getting-started)
 - [Purpose](#purpose)
 - [HTTP status codes](#http-status-codes)
 - [Using Xampp](#using-xampp)
 - [Using JQuery](#call-using-jquery)
 - [Results](#results)
 - [Methods](#methods)
    - [Start Session](#start-session)
    - [Retrieve Current Session](#retrieve-current-session)
    - [Authenticate Session](#authenticate-session)
    - [Deauthenticate Session](#deauthenticate-session)
    - [Search](#search)
    - [Server Information](#server-information)
 - [tutorial.php](#tutorial-php)


## Getting Started

---

To get started, please complete the following steps

1. Download [XAMPP](https://www.apachefriends.org/download.html) and install.

2. Copy the [Code](#tutorial.php) at the end of the page and save (as tutorial.php) in the htdocs directory from xampp (C:\xampp\htdocs).
    
3. In your browser goto `<http://localhost/tutorial.php>`


#### OR

If you prefer to call this script with JQuery, skip the above steps and see [Call using JQuery](#call-using-jquery)

 
## Purpose

---

The tutorial.php script attempts a couple simple interactions with your easydb database.

- [Start new session](#start-session)
- [Retrieve current session with session token](#retrieve-current-session)
- [Session Authentication](#authenticate-session)
- [Session Deauthentication](#deauthenticate-session)
- [Search assets](#search)
- [View server information](#server-information)


Every interaction will print a HTTP status code to the localhost page 


## HTTP status codes

---

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 500 | [Server error](/en/technical/errors): internal server error |

- _Reference_

    [HTTP Status Codes](/en/technical/api/session)


## Using XAMPP

---

Start Xampp and place tutorial.php in the htdocs directory. go to <http://localhost/tutorial.php>.

See description of Xampp at their website. <https://www.apachefriends.org/faq_windows.html>

A HTML formular will be generated. see [makePostform()](#helper-methods)

Give the easydb server URL, a valid login/email, valid password, and search criteria (optional). 

multiple search criteria may be given, separated by commas or spaces. tutorial.php will create a custom search criteria passable as a HTTP request postfield.

    
## Call using JQuery    

Use this code model to call a PHP script (with arguments) from any web application. Must have JQuery installed <https://jquery.com/download/>

Load data from the server using a HTTP POST request.

see [JQuery.post()](https://api.jquery.com/jquery.post/) for documentation.

The success callback function is passed the returned data, which will be an XML root element or a text string depending on the MIME type of the response. It is also passed the text status of the response.

We intend to post a request using Ajax and put results in a div (#results).



~~~~javascript    
 
 $(document).ready(function(){
        $("#connect").click(function(){

            $.ajax({
                type: 'POST',                                               //POST request
                url: '/tutorial.php',                                       //url where tutorial is stored
                data: { url: $("#url").val(),                               
                    login : $("#login").val(),
                    password: $("#password").val(),
                    search: $('#search').val() } ,
                        success: function(data) {
                            var tutorialresults = $(data);
                            $("#results").append(tutorialresults);          //append Tutorial results 

                }
            });
   });
});

~~~~
    
    
## Results

---

After a succesfull run, four (4) status codes will be echoed to the browser,

    200 200 200 200

followed by the informative Server Table ( see [Server Information](#server-information)), and lastly the search results. 

![The end result](tutorialResult.png "tutorial.php results")



## Methods

---

### Start Session
 
---
   
    function start_session(Session)
    
- _Parameters_

    `Object` Session

- _Return_

    void
    
- _Description_

    
    A `GET` HTTP request is made using the new_session URL without postfields 
    
    Status Code is printed to console. A 400 status code indicates an invalid URL.
    
    Session token is extracted from the response header and saved as Session.token, header is saved as Session.header, and whole response is saved as Session.content 
    

- _Reference_

    [Start a session](../../session)

- _Example_

~~~~php

function start_session($ezdb){
	
    $fields = array();                              //Initialize postfields array
    $postvars = make_postvars($fields);             //serialized the array to HTTP syntax
    
	$curlArr = curl_get($ezdb->new_session);        //call cURL get method, use new session url
    
    $ezdb->setToken($curlArr[1]);                   //Save token from the reponse body
    $ezdb->setContent($curlArr[1]);                 //Save response body
    $ezdb->setHeader($curlArr[0]);                  //Save response header
	
}

~~~~


### Retrieve Current Session

---

    function retrieve_current_session($Session)
    
- _Parameters_

    `Object` Session

- _Return_

    void
    
- _Description_

    A `GET` HTTP request is made using the new_session URL with the previously stored session token as the postfields. 
    
    Status Code is printed to console. A 400 status code indicates an invalid session token.
    
    The `instance` value from the response body is compared to the instance value from Session.content to verify that they are indeed the same session.


    
- _Reference_
    
    [Retrieve current session](https://docs.easydb.de/en/technical/api/session/#retrieve-current-session)

- _Example_


~~~~php

function retrieve_current_session($ezdb){

	$token = $ezdb->token;                      
    $fields = array('token'=>$token);               //Initialize postfields array
    $postvars = make_postvars($fields);             //serialized the array to HTTP syntax            
    
	$curlArr = curl_get($ezdb->new_session);        //call cURL get method, use new session url
	
}

~~~~

    
    
    
### Authenticate Session

---

    function authenticate_session($Session, $login, $password)
    
- _Parameters_

    `Object` Session, `String` login, `String` password

- _Return_

    void
    
- _Description_

    At runtime the user will be prompted to enter an account login/password in order for the session to be authenticated.
    
    A `POST` HTTP request is made using the auth_session URL with the session token, login, and password as postfields. 
    
    Status Code is printed to console. A 400 status code indicates an invalid login/password.
  

- _Reference_

    [Authenticate a session](http://docs.5.easydb.de/en/technical/api/session/session.html#authenticate-a-session)

- _Example_


~~~~php

function authenticate_session($ezdb, $login, $password){
	
    $fields = array('token'=>$ezdb->token,
                    'password'=>$password,
                    'login'=>$login);                        //initialize postfields array with login credentials
    $postvars = make_postvars($fields);                      //serialize the array to HTTP syntax                       
	$curlArr = curl_post($ezdb->auth_session, $postvars);    //call cURL post method, use authenitcation url
        
}

~~~~
    

### Deauthenticate Session

---

    function deauthenticate_session(Session)
    
- _Parameters_

    `Object` Session

- _Return_

    void
    
- _Description_
    
    A `POST` HTTP request is made using the deauth_session URL with the session token as the postfields. 
    
    Status Code is printed to console. A 400 status code indicates an invalid session token.

    
- _Reference_

    [Deauthenticate a session](http://docs.5.easydb.de/en/technical/api/session/session.html#deauthenticate-a-session)

- _Example_

~~~~php

function deauthenticate_session($ezdb){
    
    $fields = array('token'=>$ezdb->token);               //Initialize postfields array
    $postvars = make_postvars($fields);                   //serialized the array to HTTP syntax  
    
    $response = curl_post($ezdb->deauth_session, $postvars);    //call cURL post method, use deauthenitcation url    
    
}

~~~~

    
### Search

---

    function search($Session, $login, $password)
    
- _Parameters_

    `Object` Session, `String` login, `String` password

- _Return_

    void
    
- _Description_
    
    A `POST` HTTP request is made using the search URL with the session token and search criteria as postfields. 
    
    Status Code is printed to console. A 400 status code indicates an invalid session token.
    
    The request response is written to the locally viewable file `searchResults.txt`
  

    
- _Reference_

    [Search](https://docs.easydb.de/en/technical/api/search)




### Server Information

---

    function root_menu_about(Session)
    
- _Parameters_

    `Object` Session

- _Return_

    `String` outputTabel
    
- _Description_

    A table is produced containing relevant information to the user's easydb instance.
    
    External call are made to `getPlugins()` and `get_build_info()`, documentation on these functions can be seen below.
    
    The constructed array containing the server information will be sent to the `outputTabel()` function, which willl return an HTML formatted table as a string.
        

    
- _Reference_

    [Retrieve the list of plugins](https://docs.easydb.de/en/technical/api/plugin)

- _Example_

<table><thead><tr><th>About</th><th>Information</th></tr></thead><tbody><tr><td>api</td><td>1</td></tr><tr><td>server_version</td><td>1</td></tr><tr><td>user-schema</td><td>320</td></tr><tr><td>solution</td><td>easydb</td></tr><tr><td>name</td><td>easydb</td></tr><tr><td>db-name</td><td>easy5-easydb-user</td></tr><tr><td>Plugins</td><td>basemigration, css, custom-data-type-gnd, custom-data-type-link, easydb-export-transport-ftp, easydb-wordpress-plugin, eventmanager, hotfolder, ldap, oai, presentation-pptx, server</td></tr><tr><td>server</td><td>http://5.easydb.pf-berlin.de</td></tr><tr><td>Build</td><td>2017-06-14T14:50:09Z  @galaxy</td></tr><tr><td>5 git</td><td>8d98f7502d950be6c8786eb043799414688a65be/(detachedfrom8d98f75)</td></tr><tr><td>CUi git</td><td>8645fc4b75cd8bc8715d09c8e07f72b0c9bbaecb/(detachedfrom8645fc4)</td></tr></tbody></table>


### Helper Methods

---

    function getPlugins($ezdb)
    
Make a `GET` request to `/api/v1/plugin` url to recieve a list of installed plugins, see [Plugins](https://docs.easydb.de/en/technical/api/plugin) for details.

    function get_build_info($ezdb)

Make a `GET` request to `/web/build_info.json` url to recieve information regarding your servers build.

    function outputTabel($array) 

Formats array into HTML string

    function array_value_recursive( $key , array $arr )

Search recursively through multidimensional PHP array to find specific key-value pairs

    function print_curl_information($ch)

Helpful debug output from cURL requests, $ch is the cURL object, see [cURL](http://php.net/manual/en/curl.examples-basic.php) for more info.

    function print_curl_information_verbose($ch)
    
Helpful debug output from cURL requests, verbose.

    function make_postvars($fields)

Serialize an array into a URL formatted postfields, returns `String`

    function makePostForm()

When running from Xampp, this method will produce a formular which can be used to obtain server URL, user account credentials, and search criteria.




### tutorial.php

---

~~~~php

<?php

////
//
//	CALL FROM POST REQUEST, WITH OR WITHOUT SEARCH CRITERIA
//
////

if (empty($_POST)){

    echo makePostForm();
    
} else{

    if( isset($_POST['search']) ){
        main($_POST['url'],$_POST['login'],$_POST['password'], $_POST['search']);
        
    } else {
        main($_POST['url'],$_POST['login'],$_POST['password'], null);
    }
}

////
//
//	MAIN
//
////

function main($dbURL,$login, $password, $searchables) {
	 
	$ezdb = new Session($dbURL, $searchables);

    start_session($ezdb);
    authenticate_session($ezdb, $login, $password);
    
    echo root_menu_about($ezdb);
    
    if ($searchables) {
        echo "<div class='container-fluid'><h3>Search Results</h1>";
        echo ( search($ezdb, $login, $password));
        echo "</div>";
    }
    
}

////
//
//	SESSION OBJECT
//
////

class Session {
	
    public function __construct($server, $searchable = null,
        $searchtype = null, $searchjson = null) {
		
		$http = "http://";
		if(strpos($server, $http) !== false) {
			$http = "";
		}
		$this->server = $http . $server;
        $this->new_session = $http . $server . "/api/v1/session";
        $this->auth_session = $http . $server . "/api/v1/session/authenticate";
        $this->deauth_session = $http . $server . "/api/v1/session/deauthenticate";
        $this->search = $http . $server . "/api/v1/search";
        $this->plugins = $http . $server . "/api/v1/plugin";
        $this->buildinfo = $http . $server . "/web/build_info.json";
        $this->searchable = $searchable;
        $this->searchtype = $searchtype;
        $this->searchjson = $searchjson;
        $this->token = 0;
        $this->content = 0;
        $this->header = 0;
    }
    
    public function setToken($response) {
    
        $jsonResponse = json_decode($response, true);
        $this->token = $jsonResponse['token'];
        
    }
    
    public function setContent($response) {
    
        $jsonResponse = json_decode($response, true);
        $this->content = $jsonResponse;
        
    }
    
    public function setHeader($response) {
    
        $jsonResponse = json_decode($response, true);
        $this->header = $jsonResponse;
        
    }

}

////
//
//	HTTP REQUEST METHODS
//
////

function curl_post($url, $postvars, $searchCriteria = null) {
	
	$ch = curl_init();
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_POST, 1);                //post = 0 for a get request
	
	curl_setopt($ch,CURLOPT_POSTFIELDS,$postvars);
	
	curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch,CURLOPT_CONNECTTIMEOUT ,3);
	curl_setopt($ch,CURLOPT_TIMEOUT, 20);
    
    if (!is_null($searchCriteria)) {
        curl_setopt($ch,CURLOPT_URL,$url ."?". $postvars);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            "Content-Length: ". strlen($searchCriteria) ,
            "Content-Type: application/json" ,
            "Accept: application/json"
        ));
        curl_setopt($ch,CURLOPT_POSTFIELDS, ($searchCriteria));  
    } else {
        curl_setopt($ch, CURLOPT_HEADER, 1);
    }
    
	$response = curl_exec($ch);
    $header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    $header = substr($response, 0, $header_size);
    $body = substr($response, $header_size);
    
    if (!is_null($searchCriteria)) {
        return $response;
    }
    print_curl_information($ch) ;
	curl_close ($ch);
	return array($header, $body);

}

function curl_get($url) {
	
	$ch = curl_init();
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_POST, 0);                //post = 0 for a get request
	
	curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch,CURLOPT_CONNECTTIMEOUT ,3);
	curl_setopt($ch,CURLOPT_TIMEOUT, 20);
    curl_setopt($ch, CURLOPT_HEADER, 1);
	$response = curl_exec($ch);
    
    $header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    $header = substr($response, 0, $header_size);
    $body = substr($response, $header_size);
	print_curl_information($ch) ;
	curl_close ($ch);
	
	return array($header, $body);

}


////
//
//	TUTORIAL METHODS
//
////

function start_session($ezdb){
	
    $fields = array();
    $postvars = make_postvars($fields);
    
	$curlArr = curl_get($ezdb->new_session);
    
    $ezdb->setToken($curlArr[1]);
    $ezdb->setContent($curlArr[1]);
    $ezdb->setHeader($curlArr[0]);
	
}

function retrieve_current_session($ezdb){

	$token = $ezdb->token;
    $fields = array('token'=>$token);
    $postvars = make_postvars($fields);
    
	$curlArr = curl_get($ezdb->new_session);
	
}

function authenticate_session($ezdb, $login, $password){
	
    $fields = array('token'=>$ezdb->token,'password'=>$password, 'login'=>$login);
    $postvars = make_postvars($fields);
	$curlArr = curl_post($ezdb->auth_session, $postvars);
    
}

function deauthenticate_session($ezdb){
    
    $fields = array('token'=>$ezdb->token);
    $postvars = make_postvars($fields);
    
    $response = curl_post($ezdb->deauth_session, $postvars);
    
}

function search($ezdb, $login, $password){
	
    //making the search criteria
    $searchables = explode(",", $ezdb->searchable);
    $jsonencodedsearchablesyntax = array();   
    foreach($searchables as $s) {
        $arr = array('phrase'=> false, 'bool'=> 'must', 'mode'=> 'fulltext', 'string'=>$s, 'type'=> 'match');
        array_push($jsonencodedsearchablesyntax, $arr);
        
    }
    
    $fields = array('token'=>$ezdb->token);
    $jsonencodedsearchablesyntax = json_encode(array('search'=>$jsonencodedsearchablesyntax) );
    $postvars = make_postvars($fields);
	$curlArr = curl_post($ezdb->search, $postvars, $jsonencodedsearchablesyntax );
    
    
    $curlArr = json_decode($curlArr, true);
    
    
    $basenames = (array_value_recursive('original_filename',$curlArr));
    $originalnames = array_value_recursive('name',$curlArr);
    $result = "<p>";
    $count = 0;
    
    if (is_array($basenames)) {
        foreach($basenames as $bn) {
            $result .= $bn . "<br>";
            $count ++;
        }
    }
    if (is_array($originalnames)) {
        foreach($originalnames as $on) {
            $result .= $on . "<br>";
            $count ++;
        }
    }
    
    
    $result .= "Total Count : " . $count  . "<br>";
    $result .= "</p>";
    return  $result;

}




function root_menu_about($ezdb) {

    $aboutDetails = array("api" , "server_version" , "user-schema" , "solution" , "instance", "db-name", "Plugins",   "server", "Build", '5 git', 'CUi git');
    $outputArray =[];
    $buildinfo = get_build_info($ezdb);
    
    foreach($aboutDetails as $element) {
            
            if ($element == "instance") {$element = "name";}
            else if ($element == "Plugins") {$info = getPlugins($ezdb);}
            else if ($element == "server") {$info = $ezdb->server;}
            else if ($element == "last-modified") {$info = $ezdb->header["last-modified"];}
            else if ($element == "Build") {$info = gmdate("Y-m-d\TH:i:s\Z", $buildinfo["date"] ). "  @". $buildinfo["host"];}
            else if ($element == "5 git") {$info = $buildinfo["ez5"] ;}
            else if ($element == "CUi git") {$info = $buildinfo["cui"]; }
            else {
                $info = $ezdb->content['instance'][$element];
            }
            array_push($outputArray, array("About" =>$element, "Information" => $info));
    }
    return outputTabel($outputArray);
    
}



////
//
//	HELPER FUNCTIONS
//
////

function getPlugins($ezdb){
    $curlArr = curl_get($ezdb->plugins);
    $plugins = json_decode($curlArr[1], true);
    $plugins = $plugins['plugins'];
    $plgnstring = "";
    foreach ($plugins as $plgn) {
        $plgnstring  .= $plgn['name'] . ", ";
    }
    return rtrim($plgnstring,", ");
}

function get_build_info($ezdb){

    $curlArr = curl_get($ezdb->buildinfo);
    $buildinfo = json_decode($curlArr[1], true);
    return $buildinfo;
}



function array_value_recursive($key, array $arr){
    $val = array();
    array_walk_recursive($arr, function($v, $k) use($key, &$val){
        if($k == $key) array_push($val, $v);
    });
    return count($val) > 1 ? $val : array_pop($val);
}



function outputTabel($data) {
    $outputTabelHTML = "";
    $outputTabelHTML .= '<table><thead><tr>';
    
    
        $outputTabelHTML .= '<th>' . 'About' . '</th>';
        $outputTabelHTML .= '<th>' . 'Information' . '</th>';
    
    $outputTabelHTML .= '</tr></thead><tbody>';
    
    foreach ($data as $row) {
        $outputTabelHTML .= '<tr>';
        $outputTabelHTML .= '<td>' . $row['About'] . '</td>';
        $outputTabelHTML .= '<td>' . $row['Information'] . '</td>';
        $outputTabelHTML .= '</tr>';
    }
    
    
    $outputTabelHTML .= '</tbody></table>';
    return $outputTabelHTML;  
}

function print_curl_information($ch) {
    echo "\r\n" . curl_getinfo($ch, CURLINFO_HTTP_CODE);
    }

function print_curl_information_verbose($ch) {
    
    if (!curl_errno($ch)) {
      $info = curl_getinfo($ch);
      echo 'Took ', $info['total_time'], ' seconds to send a request to ', $info['url'], "\n";
    }   
    if (!curl_errno($ch)) {
        switch ($http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE)) {
        case 200:  # OK
          echo $http_code;
          break;
        default:
          echo 'Unexpected HTTP code: ', $http_code, "\n";
    }
    } else {
        echo 'Curl error: ' . curl_error($ch);
        $info = curl_getinfo($ch);
          echo 'Took ', $info['total_time'], ' seconds to send a request to ', $info['url'], "\n";
    }
    
}


function make_postvars($fields) {

	$postvars = '';
	foreach($fields as $key=>$value) {
	$postvars .= $key . "=" . $value . "&";
	}
    return substr($postvars, 0,-1);
}
 

 
function makePostForm(){
    $search = 'search';
    $form = '<!DOCTYPE html>
<html lang="en">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

<style>
input[type=text], select, textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */  
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

input[type=submit] {
    background-color: #00BFFF;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type=submit]:hover {
    background-color: #00addd;
}

.container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
}
</style><div class="container-fluid">
<form action="/tutorial.php" method="post">

<label for="url">easydb URL</label>
<input type="text" id="url" name="url" placeholder="http://5.easydb.de">

<label for="login">LOGIN</label>
<input type="text" id="login" name="login" placeholder="username/email..">

<label for="password">PASS</label>
<input type="text" id="password" name="password" placeholder="password..">

<label for="search">Search</label>
<input type="text" id="search" name="search"  placeholder="*optional*" />

<input type="submit" value="RUN"></form></div></html>';

return $form;

}
 
 
////
//	error_message
////


function server_url_error_message($str, $err){
    echo "URL is invalid";
    echo "{0} raises {1}".format($str, $err);
    
}

function command_line_error_message(){
    echo "Value must be entered in for -server and -search or -searchjson";
    echo "Please run again";
    
}

function search_criteria_error_message(){
    echo "input search criteria does not exist";
    echo "please check for spelling errors or move file closer to session.py directory";
    
}

function doNothing($e) {
    //doing nothing
    echo "<script>console.log('doing nothing!');</script>";
    
}

?>

~~~~


