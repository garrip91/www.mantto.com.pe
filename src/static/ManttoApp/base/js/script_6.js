(function($) {
    jQuery(window).on('resize', function() {
        if ($(window).width() >= 992) {
            $('#page').css('padding-bottom', $('.uncover .bottom-wrapper').outerHeight());
        }
    });
    jQuery(window).on('load', function() {
        jQuery(window).trigger('resize');
    });
})
(jQuery);