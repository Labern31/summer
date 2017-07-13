$(document).ready(function(){
var isHidden = false;

    $("#clicker").click( function (){
        if(isHidden==false){
            $("#hidden").fadeTo(1000, 0.1);
            isHidden=true;
            }
            else{
             $("#hidden").fadeTo(1000, 0.9);
            isHidden=false;
            }
    });

    $('#my_name').t({
        speed:70,
        blink:400,
        mistype:1,
        pause_on_click:true
        });

    })