$('html').on('click', '.markdown-section img', function(){
	var popover = document.createElement('div');
	popover.classList.add("popover");
	// faux close button - the popover can be closed by clicking anywhere
	var close = document.createElement('div');
	close.innerText = "×";
	popover.appendChild(close);
	var image = new Image();
	image.classList.add("popover-image");
	image.src = this.src;
	popover.appendChild(image);
	popover.addEventListener("click", function(){ jQuery(this).remove(); });
	$("body").append(popover);
});