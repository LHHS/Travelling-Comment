function resizePages() {
    var h = $(window).height();
    var height = h < 600 ? 600 : h;
    $('section').css('height',height);
    $('.spirits').css('height',height*1.5);
    $('.staff').removeAttr('style');
}
    $(".info-animate").hover(function(){
    $(this).addClass('animated ' + $(this).data('action'));
    });

    $(".info-animate").bind("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd",function(){
    $(this).removeClass('animated ' + $(this).data('action'));
});

