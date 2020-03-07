$(document).ready(function(){
    let numClick = 0
    $(".bgCol").click(function(){
        if (numClick == 0){
            $(".bgCol").css("backgroundColor", "cyan")
                     .css("width", "75%");
            numClick = 1
        }
        else if (numClick == 1){
            $(".bgCol").css("backgroundColor", "white")
            numClick = 0
        }
    });
});
