$(document).ready(function(){

    // Change "NGUYEN GIA HIEN TU", "EDUCATION", "ETRACURRICULAR ACTIVITIES" background color
    let numClick = 0
    $(".bgCol").mouseenter(function(){
        if (numClick == 0){
            $(".bgCol").css("backgroundColor", getRandomColor())
                       .css("width", "75%");
            numClick = 1
        }
        else if (numClick == 1){
            $(".bgCol").css("backgroundColor", "white")
            numClick = 0
        }
    });

   function getRandomColor() {
    var letters = '9ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 7)];
        }
    return color;
    }

    // Hide and Show "Skills" and "Awards"
    $("#name").click(function(){
        $("#info").slideToggle(500);
    });

    $("#skill").click(function(){
        $("#skills").fadeToggle(500);
    });

    $("#award").click(function(){
        $("#awards").toggle(500);
    });

    $("#Edu").click(function(){
        $("#Education").animate({
            height: 'toggle',
            width: 'toggle'
        });
    });

    $("#ExtraAct").click(function(){
        $(".Activities").slideToggle(500);
    });

    // Change image
    function imageLooping() {
        let rotator = document.getElementById('image'),     //get the element
            dir = 'Resume Images/',                         //images folder
            num = 1,                                        //start number
            len = 3;                                        //limit
        setInterval(function(){                             //interval changer
            rotator.src = dir + num +'.jpg';                //change picture
            num = (num == len-1) ? 0 : ++num;               //reset if last image reached
        }, 3000);
    };
    imageLooping();

    // Alert
    $("img").dblclick(function(){
        alert("Please don't hit me :(");
    });
});

