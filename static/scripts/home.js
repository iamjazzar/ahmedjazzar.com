
'use strict';

var body = $( 'body' );
var nightImg = $( '#night-img' );
var dayImg = $( '#day-img' );
var imacImg = $( '#imac-img' );
var section = $( '#section' );
var navContainer = $( '#toggle' );
var navOverlay = $( '#nav-overlay' );
var scrollTop = $( '.scroll-top' );

var xp = 0;
var mouseX = 0;
var relMouseX = 0;
var windowCenterX = 0;
var frameRate =  0;
var timeInterval = Math.round( 1000 / frameRate );
var loop = 0;

// iMac Animation
section.mouseenter(function(){

  nightImg.css({opacity: 1});
  dayImg.css({opacity: 1});
  imacImg.css({opacity: 0});

  section.mousemove(function(e){
    mouseX = e.pageX;
    windowCenterX = $(window).width() / 2;
    relMouseX = mouseX - windowCenterX;
  });

  loop = setInterval(function(){
    xp += (relMouseX - xp) / 15;

    dayImg.css({width: 470 - (xp - 470) * 0.5, right: (xp - 470) * 0.5});
    nightImg.css({width: 469 - (469 - xp) * 0.5, left: (469 - xp) * 0.5});

  }, timeInterval );
}).mouseleave(function(){
		// reset the imac to initial state
    imacImg.css({opacity: 1});
    dayImg.css({opacity: 0});
    nightImg.css({opacity: 0});
	});



// toggle nav menu
navContainer.click(function() {
  $(this).toggleClass( 'active' );
  navOverlay.toggleClass( 'open' );
});


// scroll top hover
scrollTop.hover(
  function () {
    $( '.fa-angle-up' ).toggleClass( 'floating' );
});


// scroll to top
$( 'a[href^="#header"]' ).on( 'click', function(e) {

   e.preventDefault();
   var hash = this.hash;

   body.animate({
       scrollTop: $(hash).offset().top
     }, 1000, function(){
   });
 });
