// Dropdown Functionality
document.addEventListener("DOMContentLoaded", function() {
    var dropdowns = document.querySelectorAll(".dropdown");
  
    // Add event listener to each dropdown
    dropdowns.forEach(function(dropdown) {
      var dropdownContent = dropdown.querySelector(".dropdown-content");
  
      // Show dropdown content on hover
      dropdown.addEventListener("mouseover", function() {
        dropdownContent.style.display = "block";
      });
  
      // Hide dropdown content when not hovering
      dropdown.addEventListener("mouseout", function() {
        dropdownContent.style.display = "none";
      });
    });
  });
  