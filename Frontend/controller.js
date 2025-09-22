$(document).ready(function () {
    eel.expose(displayMessage);
    function displayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate("start");
    }

    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        //siriWave.stop();
    }
});


