$('html').on('click', '.markdown-section img', function(){
	var popover = document.createElement('div');
	popover.classList.add("popover");
	var image = new Image();
	image.classList.add("popover-image");
	image.src = this.src;
	popover.appendChild(image);
	popover.addEventListener("click", function(){ jQuery(this).remove(); });
	$("body").append(popover);
});