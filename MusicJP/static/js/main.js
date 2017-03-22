/*Home selection*/
$( "h1 + ul > li" ).on( "click", function() {

    $(this).next().slideToggle();
    var span = $(this).find("span");
    if ($(span).hasClass("glyphicon-plus")){
        $(span).removeClass("glyphicon-plus");
        $(span).addClass("glyphicon-menu-up");
    }else {
        $(span).removeClass("glyphicon-menu-up");
        $(span).addClass("glyphicon-plus");
    }
});