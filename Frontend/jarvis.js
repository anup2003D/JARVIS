$(document).ready(function(){
    $('.text').textillate({
        loop:true,
        speed:1500,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        }
    })
    
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 940,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    height: 400,
    autostart: true,
    waveColor: "#00ff00",
    waveOffset: 0,
    rippleEffect: true,
    rippleColor: "#ffffff",
  });

  // Update siri message animation settings
  $('.siri-message').textillate({
        loop: true,
        minDisplayTime: 2000,
        initialDelay: 0,
        autoStart: true,
        in: {
            effect: 'fadeInUp',
            delayScale: 1.5,
            delay: 50,
            sync: true,
            shuffle: false,
        },
        out: {
            effect: 'fadeOutUp',
            delayScale: 1.5,
            delay: 50,
            sync: true,
            shuffle: false,
        },
        callback: function() {},
        type: 'char'
    });

    // Play initial sound when page loads
    if(typeof eel !== "undefined"){
        eel.play_assistant_sound();
    }

    $("#MicBtn").click(function () { 
        // Hide oval and show siriwave
        eel.play_assistant_sound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takeAllCommands()();
        //siriWave.start();

        // Play sound when mic button is clicked
        /*if(typeof eel !== "undefined"){
            await eel.play_assistant_sound()();
            // Start speech recognition after sound plays
            await eel.takeCommand()();
        } else {
            console.error("Eel is not defined");
        }*/
    });


    function doc_keyUp(e){

        if(e.key==='j' && e.metaKey){
            eel.play_assistant_sound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.takeAllCommands()();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message){
        if(message != ""){
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.takeAllCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }

    function ShowHideButton(message){
        if(message.length==0){
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
        }
        else{
        $("#MicBtn").attr("hidden", true);
        $("#SendBtn").attr("hidden", false);
        }
    }

    $("#chatbox").keyup(function(){
        let message  =$("#chatbox").val();
        ShowHideButton(message);
    });

    $("#SendBtn").click(function(){
        let message  =$("#chatbox").val();
        PlayAssistant(message);
    });

    $("#chatbox").keypress(function(e){
        if(e.which==13){
            let message  =$("#chatbox").val();
            PlayAssistant(message);
        }
    });

});
