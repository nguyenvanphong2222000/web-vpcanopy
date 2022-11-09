var a= 'static/images/1.jpg'
        function display_image1(){
            function display_image(src) {
                var a = document.createElement("img");
                a.src = src;
                var t = document.createTextNode("body {position: relative; left: 0px; top: 10px;height: 200px;width: 300px;}");
                a.appendChild(t);
                document.body.appendChild(a);
            }
            return display_image(a)
        }

        
    // function myFunction() {
    //     setInterval(function(){
    //     }, 1000) 
    // }
