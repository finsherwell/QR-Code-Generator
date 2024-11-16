document.getElementById("url-form").addEventListener("submit", function (event) {
    // Get the settings form elements
    const fileType = document.querySelector("select[name='filetype']");
    const downloadName = document.querySelector("input[name='download_name']");
    const fillColor = document.querySelector("input[name='fill_color']");
    const backColor = document.querySelector("input[name='back_color']");
    const errorMessage = document.getElementById("error-message");
  
    // Check if all settings are filled out
    if (
      !fileType.value ||
      !downloadName.value.trim() ||
      !fillColor.value ||
      !backColor.value
    ) {
      // Prevent form submission
      event.preventDefault();
  
      // Show the error message
      errorMessage.classList.remove("hidden");
    } else {
      // Hide the error message if everything is fine
      errorMessage.classList.add("hidden");
    }
  });
  