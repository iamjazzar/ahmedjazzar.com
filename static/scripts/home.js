
'use strict';

var body = $( 'body' );
var nightImg = $( '#night-img' );
var imacContainer = $( '#imac-container' );
var navContainer = $( '#toggle' );
var navOverlay = $( '#overlay' );
var scrollTop = $( '#scroll-top' );
var nightBackground = $( '#night-bg' );
var dayBackground = $( '#day-bg' );
var imac = $( '#imac' );

var imageWidth = 430;
var xp = 0;
var xpHigh = imageWidth;
var xpLow = -imageWidth;
var mouseX = 0;
var relMouseX = 0;
var windowCenterX = 0;
var timeInterval = 500;
var loop = 0;
var relativeWidth = 0;

// iMac Animation
imacContainer.hover(function(){
  $(this).mousemove(function(e){
    mouseX = e.pageX;
    windowCenterX = $(window).width() / 2;
    relMouseX = mouseX - windowCenterX;
  });

  nightImg.stop();
  imac.stop();
  loop = setInterval(function(){
    xp += 10 * (relMouseX - xp) / timeInterval;
    xp = Math.max(xpLow, Math.min(xp, xpHigh));
    relativeWidth = (imageWidth + xp) * 0.5;

    nightImg.css({width: (imageWidth + xp) * 0.5, left: (imageWidth - xp) * 0.5});
    imac.css({right: xp/25});

    var relativeOpacity = 2 * relativeWidth/imageWidth;
    nightBackground.css({opacity: relativeOpacity});
    dayBackground.css({opacity: 2 - relativeOpacity});
  });
}, function(){
  clearInterval(loop);
  xp = 0;
  nightImg.animate({width: imageWidth * 0.5, left: imageWidth * 0.5}, timeInterval);
  nightBackground.css({opacity: 1});
  dayBackground.css({opacity: 1});
  imac.animate({right: 0}, timeInterval);
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
