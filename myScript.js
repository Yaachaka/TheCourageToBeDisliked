const stylesheet = window.getComputedStyle(document.documentElement);

// View content
const viewContent = document.getElementById("id-view-content");
// Attach an event listener to the element.
viewContent.addEventListener("click", function() {
	const widthLeft = stylesheet.getPropertyValue("--widthLeft");
	if(widthLeft == "0vw")
	{
		document.documentElement.style.setProperty("--widthLeft", "20vw");
	}
	else
	{
		document.documentElement.style.setProperty("--widthLeft", "0vw");
	}
});
