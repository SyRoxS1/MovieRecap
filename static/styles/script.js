document.addEventListener("DOMContentLoaded", function() {
    // Wait for the DOM content to be fully loaded
    var slideElem = document.querySelector(".slide-elem");

    // Add the "triggered" class after a short delay
    setTimeout(function() {
        slideElem.classList.add("triggered");
    }, 100); // Adjust the delay as needed
});
