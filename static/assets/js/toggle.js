document.addEventListener("DOMContentLoaded", function () {
    const settingsButton = document.getElementById("settings-button");
    const settingsDropdown = document.getElementById("settings-dropdown");

    settingsButton.addEventListener("click", function (event) {
        event.stopPropagation(); // Prevent click from propagating
        const isVisible = settingsDropdown.style.display === "block";
        settingsDropdown.style.display = isVisible ? "none" : "block";
    });

    // Close the dropdown when clicking outside
    document.addEventListener("click", function () {
        settingsDropdown.style.display = "none";
    });
});