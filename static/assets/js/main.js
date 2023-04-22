"user strict";

$(document).ready(function () {
	//--Owl Carousel--//
	$(".banner-wrapper").owlCarousel({
		loop: true,
		margin: 0,
		smartSpeed: 2500,
		autoplayTimeout: 2000,
		autoplay: false,
		nav: false,
		dots: false,
		responsiveClass: true,
		navText: [
			'<i class="fas fa-chevron-left"></i>',
			'<i class="fas fa-chevron-right"></i>',
		],
		responsive: {
			0: {
				items: 1,
			},
			500: {
				items: 1,
			},
			767: {
				items: 1,
			},
			991: {
				items: 1,
			},
			1199: {
				items: 1,
			},
			1399: {
				items: 1,
			},
		},
	});
	$(".progress-slider").owlCarousel({
		loop: true,
		margin: 10,
		smartSpeed: 2500,
		autoplayTimeout: 2500,
		autoplay: false,
		nav: true,
		dots: true,
		responsiveClass: true,
		navText: [
			'<i class="fas fa-chevron-left"></i>',
			'<i class="fas fa-chevron-right"></i>',
		],
		responsive: {
			0: {
				items: 1,
			},
			575: {
				items: 1,
			},
			767: {
				items: 1,
			},
			991: {
				items: 2,
			},
			1199: {
				items: 1,
			},
			1499: {
				items: 2,
			},
			1999: {
				items: 2,
			},
		},
	});
	$(".virtual-wrap").owlCarousel({
		loop: true,
		margin: 20,
		smartSpeed: 2500,
		autoplayTimeout: 3000,
		autoplay: false,
		nav: true,
		dots: false,
		responsiveClass: true,
		navText: [
			'<i class="fas fa-chevron-left"></i>',
			'<i class="fas fa-chevron-right"></i>',
		],
		responsive: {
			0: {
				items: 1,
			},
			400: {
				items: 2,
			},
			767: {
				items: 3,
			},
			991: {
				items: 4,
			},
			1199: {
				items: 3,
			},
			1399: {
				items: 4,
			},
			1499: {
				items: 4,
			},
			1699: {
				items: 4,
			},
		},
	});
	$(".sponsor-wrap").owlCarousel({
		loop: true,
		margin: 20,
		smartSpeed: 2000,
		autoplayTimeout: 2000,
		autoplay: false,
		nav: false,
		dots: false,
		responsiveClass: true,
		navText: [
			'<i class="fas fa-chevron-left"></i>',
			'<i class="fas fa-chevron-right"></i>',
		],
		responsive: {
			0: {
				items: 2,
			},
			400: {
				items: 3,
			},
			575: {
				items: 4,
			},
			767: {
				items: 5,
			},
			991: {
				items: 6,
			},
			1199: {
				items: 5,
			},
			1499: {
				items: 9,
			},
		},
	});
	//--Owl Carousel--//
	
	// password hide
	$(".toggle-password, .toggle-password2, .toggle-password3, .toggle-password4, .toggle-password5").click(function() {
		$(this).toggleClass("fa-eye fa-eye-slash");
		var input = $($(this).attr("id"));
		if (input.attr("type") == "password") {
			input.attr("type", "text");
		} else {
			input.attr("type", "password");
		}
	});
	//Toast
	

	//right menu close
	var closebtns = document.getElementsByClassName("close-items");
	var i;
	for (i = 0; i < closebtns.length; i++) {
	closebtns[i].addEventListener("click", function() {
		this.parentElement.style.display = 'none';
	});
	}
	//--Nice Select--//
	$('select').niceSelect();
	
	$(document).click(function() {
		$('.dropdown-menu.show').removeClass('show');
	});
	$('body').on('click','.apto-trigger-dropdown', function(e){
		e.stopPropagation();
		$(this).closest('.apto-dropdown-wrapper').find('.dropdown-menu').toggleClass('show');
	});
	$('body').on('click','.dropdown-item', function(e){
		e.stopPropagation();
		let $selectedValue = $(this).val(); 
		let $icon          = $(this).find('svg');
		let $btn           = $(this).closest('.apto-dropdown-wrapper').find('.apto-trigger-dropdown');
		
		$(this).closest('.apto-dropdown-wrapper').find('.dropdown-menu').removeClass('show').attr('data-selected', $selectedValue);
		$btn.find('svg').remove();
		$btn.prepend($icon[0].outerHTML);
		
	});
	//--Nice Select--//


	//--Progress Bar--//
	$(".animated-progress span").each(function () {
		$(this).animate(
		  {
			width: $(this).attr("data-progress") + "%",
		  },
		  1000
		);
		$(this).text($(this).attr("data-progress") + "%");
	  });
	//--Progress Bar--//

	$(function() {
		$('.hamburger, .hamb').click(function () {
		  showHideMobile();
		});
		
		$(".dimmer").click(function() {
		  showHideMobile();
		});
		
		$('li .icon-arrow').click(function () {
		  $(this).parent().parent().toggleClass('showSubmenu');
		});
	  });
	  
	function showHideMobile() {
	$(".hamburger, .hamb").toggleClass('active act');
	$(".hamburger, .hamb").parent('.menu').toggleClass('active act');
	$('.dimmer').toggleClass('active act');
	$('body').toggleClass('no-scrolling');
	}

	/* Tab Section Js area */
	$(".header-bar").on("click", function (e) {
		$(".main-menu, .header-bar").toggleClass("active act");
	});
	$(".main-menu li a").on("click", function (e) {
		var element = $(this).parent("li");
		if (element.hasClass("open")) {
			element.removeClass("open");
			element.find("li").removeClass("open");
			element.find("ul").slideUp(300, "swing");
		} else {
			element.addClass("open");
			element.children("ul").slideDown(300, "swing");
			element.siblings("li").children("ul").slideUp(300, "swing");
			element.siblings("li").removeClass("open");
			element.siblings("li").find("li").removeClass("open");
			element.siblings("li").find("ul").slideUp(300, "swing");
		}
	});
	$(".scrollToTop").on("click", function () {
		$("html, body").animate(
			{
				scrollTop: 0,
			},
			700
		);
		return false;
	});


	/*-------- Magnific Popup Start--------*/
	$('.video-btn').magnificPopup({
		type: 'iframe',
		callbacks: {
			
	  	}
	});
/*-------- Magnific Popup Start--------*/

	//free popup
	$(".Click-here").on('click', function() {
		$(".custom-model-main").addClass('model-open');
	}); 
	$(".close-btn, .bg-overlay").click(function(){
		$(".custom-model-main").removeClass('model-open');
	});

	$(".click-heretwo").on('click', function() {
		$(".referral-model-main").addClass('model-open');
	}); 
	$(".close-btn, .bg-overlay").click(function(){
		$(".referral-model-main").removeClass('model-open');
	});
	//free popup
	  
	//Click event to scroll to top end

	/*-- Odometer Counting Start--*/
	$(".odometer-item").each(function () {
		$(this).isInViewport(function (status) {
			if (status === "entered") {
				for (
					var i = 0;
					i < document.querySelectorAll(".odometer").length;
					i++
				) {
					var el = document.querySelectorAll(".odometer")[i];
					el.innerHTML = el.getAttribute("data-odometer-final");
				}
			}
		});
	});
	/*-- Odometer Counting End--*/

	/*-- Woe Animation Start--*/
	new WOW().init();
	/*-- Wow Animation End--*/

	/*-- Preloader Start--*/
	setTimeout(function(){
		$('.boxes-bg').fadeToggle();
	}, 2000);
	/*-- Preloader End--*/
	//Search Click
	$(document).ready(function(){
		$('a[href="#search"]').on('click', function(event) {                    
			$('#search').addClass('open');
			$('#search > form > input[type="search"]').focus();
		});            
		$('#search, #search button.close').on('click keyup', function(event) {
			if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
				$(this).removeClass('open');
			}
		});            
	});

	//Timing Hours
	$(".countdown").each(function () {
		var date = $(this).data("date");
		$(this).countdown({
			date: date,
			offset: +6,
			day: "Day",
			days: "Days",
		});
	});	
	//Quantity number
});
//dark light
$(".mode--toggle").on("click", function () {
	setTheme(localStorage.getItem("theme"));
});
if (localStorage.getItem("theme") == "light-theme") {
	localStorage.setItem("theme", "dark-theme");
} else {
	localStorage.setItem("theme", "light-theme");
}
setTheme(localStorage.getItem("theme"));
function setTheme(theme) {
	if (theme == "dark-theme") {
		localStorage.setItem("theme", "light-theme");
		$("html").addClass(theme);
		$(".mode--toggle").find("img").attr("src", "assets/img/moon.png");
	} else {
		localStorage.setItem("theme", "dark-theme");
		$("html").removeClass("dark-theme");
		$(".mode--toggle").find("img").attr("src", "assets/img/sun.png");
	}
}






