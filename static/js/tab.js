$(function() {
	$('.tabs li').on('click', function() {
		var tabId = $(this).attr('data-tab');

		$('.tabs li').removeClass('current'); 
		$('.tab-pane').removeClass('current'); 

		$(this).addClass('current');
		$('#' + tabId).addClass('current');
	});
});