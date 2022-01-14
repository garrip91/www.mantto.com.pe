jQuery(document).ready(function ($) {
	var $window = $(window); // Scroll up
	var $scrollup = $('.scrollup');

	$window.scroll(function () {
		if ($window.scrollTop() > 100) {
			$scrollup.addClass('show');
		}
		else {
			$scrollup.removeClass('show');
		}
	});

	$scrollup.on('click', function (evt) {
		$("html, body").animate({scrollTop: 0}, 600);
		evt.preventDefault();
	});
});