
var map, // the map id
		mapProp,  // map type 
    mapZoom=15,
    // center
		mapCenter=new google.maps.LatLng(50.645107,11.140137),
		// points
 		pointA = new google.maps.LatLng(35.6999872,51.3090523), // basel airport
    pointB = new google.maps.LatLng(29.5460138,52.5901623), // frankfurt airport
pointE = new google.maps.LatLng(29.5460138,57.5901623),

    // pointC = new google.maps.LatLng(52.370216,4.895168), // amsterdam
    // pointD= new google.maps.LatLng(69.649205, 18.955324), // Tromsø
    // stroke options
    strokeColor="#118c8b",
    strokeSize=5,
    strokeOpacity=.8;




     var acfb = new google.maps.LatLng(29.5460138,52.5901623);

      var georgiaTech = new google.maps.LatLng(35.6899872,51.3090523);
      var georgiaTech1 = new google.maps.LatLng(35.6999872,51.3090523);
      var kashan = new google.maps.LatLng(33.9814066, 51.3427133);
      var center = new google.maps.LatLng(33.9814066, 51.0);
      var latLngArray = [acfb, georgiaTech];
      var map;
    
      var directionsDisplay;
      var directionsDisplay1;

      var directionsService = new google.maps.DirectionsService();
      var rendererOptions = {
    suppressMarkers: false,
      };

function drawCurve(P1, P2, map) {
  var lineLength = google.maps.geometry.spherical.computeDistanceBetween(P1, P2);
  var lineHeading = google.maps.geometry.spherical.computeHeading(P1, P2);
  if (lineHeading < 0) {
    var lineHeading1 = lineHeading + 25;
    var lineHeading2 = lineHeading + 155;
  } else {
    var lineHeading1 = lineHeading + -25;
    var lineHeading2 = lineHeading + -155;
  }
  var pA = google.maps.geometry.spherical.computeOffset(P1, lineLength / 2.2, lineHeading1);
  var pB = google.maps.geometry.spherical.computeOffset(P2, lineLength / 2.2, lineHeading2);

  var curvedLine = new GmapsCubicBezier(P1, pA, pB, P2, 0.01, map);
}




	
function initialize(){
	 // define properties

    //   LatLng = google.maps.LatLng
    //   Marker = google.maps.Marker

    // var pos1 = new LatLng( 35.6899882, 51.3090523);
    // var pos2 = new LatLng(29.6652806, 52.2528142);
    // var markerP1 = new Marker({
    //     position: pos1,
    //     label: "1",
    //     draggable: true,
    //     map: map
    // });
    // var markerP2 = new Marker({
    //     position: pos2,
    //     label: "22222222222",
    //     draggable: true,
    //     map: map});



   mapProp = {center:mapCenter,
    zoom:mapZoom,
     mapTypeId:google.maps.MapTypeId.ROADMAP};  
   // set the map
	 map = new google.maps.Map(document.getElementById("map-canvas"),mapProp);
  // drawCurves 

	drawCurve(pointA, pointB, map);
	// drawCurve(pointC, pointD, map);

          directionsDisplay = new google.maps.DirectionsRenderer({
              rendererOptions,
              polylineOptions: {
                strokeColor: "green",
                strokeOpacity: 0

              },

      suppressMarkers: false,

  })
        ;
                directionsDisplay1 = new google.maps.DirectionsRenderer({
        
              polylineOptions: {
                strokeColor: "#3385ff",
                strokeOpacity: 0.7,
                strokeWeight: 6

              },

      suppressMarkers: true
  })
        ;

        var mapOptions = {
          center: center,
          zoom: 5
          // scaleControl: true
        };
        // map = new google.maps.Map(document.getElementById('map-canvas'),
            // mapOptions);
        directionsDisplay.setMap(map);
        directionsDisplay1.setMap(map);
        // directionsDisplay.setPanel(document.getElementById('directionsPanel'));

        // var markerArray = [];

        // for (var i=1; i<2; i++) {
        //   var marker = new google.maps.Marker({
        //       position: latLngArray[i],
        //       animation: google.maps.Animation.DROP,
        //       title: "Location: " + i
        //     });

        //   marker.setMap(map);

        //   markerArray.push(marker);
        // }
        makeRoute1();

var styledMapType = new google.maps.StyledMapType([{
  }]);

map.mapTypes.set('styled_map', styledMapType);
  map.setMapTypeId('styled_map');

  // var contentString = '<div class="iw-content">' + '<div class="iw-subTitle">My company </div>' + '<p>455 street</p>' + '<p>City, World</p>' + '<p>Canada, Postalcode</p>' + '</div>';

  // var infowindow = new google.maps.InfoWindow({
  //   content: contentString
  // });





        // makeRoute1();
}

// google.maps.event.addDomListener(window, 'load', initialize);
// original Belzier Curve code from nicoabie's answer to this question on StackOverflow:
// http://stackoverflow.com/questions/5347984/letting-users-draw-curved-lines-on-a-google-map
var GmapsCubicBezier = function(latlong1, latlong2, latlong3, latlong4, resolution, map) {
  var lat1 = latlong1.lat();
  var long1 = latlong1.lng();
  var lat2 = latlong2.lat();
  var long2 = latlong2.lng();
  var lat3 = latlong3.lat();
  var long3 = latlong3.lng();
  var lat4 = latlong4.lat();
  var long4 = latlong4.lng();

  var points = [];

  for (var it = 0; it <= 1; it += resolution) {
    points.push(this.getBezier({
      x: lat1,
      y: long1
    }, {
      x: lat2,
      y: long2
    }, {
      x: lat3,
      y: long3
    }, {
      x: lat4,
      y: long4
    }, it));
  }
  var path = [];
  for (var i = 0; i < points.length - 1; i++) {
    path.push(new google.maps.LatLng(points[i].x, points[i].y));
    path.push(new google.maps.LatLng(points[i + 1].x, points[i + 1].y, false));
  }

  var FlightLine = new google.maps.Polyline({
    path: path,
    geodesic: true,
    strokeColor:strokeColor,
    strokeOpacity:0,
    strokeWeight:strokeSize,

    icons:  [{
      icon: {
        path: 'M 0,-1 0,1',
        strokeOpacity: strokeOpacity,
        scale: strokeSize
      },
      offset: '0',
      repeat: '2px'
    }], 
  });


      function addLine() {
        FlightLine.setMap(map);
      }

      function removeLine() {
        FlightLine.setMap(null);
      }




  // FlightLine.setMap(map);
// var radiosSmoking = document.getElementsByName('tours');
//         if (radiosSmoking[0].checked) {
//             return addLine()
//         } else if (radiosSmoking[1].checked) {
//             return removeLine()
//         }

        


        // var radiosSmoking = document.getElementsByName('tours');
        // if (radiosSmoking[0].checked) {
        //     FlightLine.setMap(null)
        // } else if (radiosSmoking[1].checked) {
            


//           google.maps.event.addListener(FlightLine, '', function() {

// removeLine()
//           });







// for(radio in document.getElementsByName('tours')) {
//     document.getElementsByName('tours')[radio].onclick = function() {
//         removeLine()
//     }
// }

FlightLine.setMap(map)
        // }

}
GmapsCubicBezier.prototype = {

  B1: function(t) {
    return t * t * t;
  },
  B2: function(t) {
    return 3 * t * t * (1 - t);
  },
  B3: function(t) {
    return 3 * t * (1 - t) * (1 - t);
  },
  B4: function(t) {
    return (1 - t) * (1 - t) * (1 - t);
  },
  getBezier: function(C1, C2, C3, C4, percent) {
    var pos = {};
    pos.x = C1.x * this.B1(percent) + C2.x * this.B2(percent) + C3.x * this.B3(percent) + C4.x * this.B4(percent);
    pos.y = C1.y * this.B1(percent) + C2.y * this.B2(percent) + C3.y * this.B3(percent) + C4.y * this.B4(percent);
    return pos;
  }
};







        function makeRoute1() {
        var selectedMode = document.getElementById("mode1").value;
        // directionsDisplay1.setMap(null);


        var request1 = {
          origin: acfb,
          destination: georgiaTech,
          
          waypoints: [
                      {
              location:"shiraz airport",
              stopover:true,
              
            },
            {
              location:"isfahan",
              stopover:true
            },
                        {
              location:"kashan",
              stopover:true
            },
            

          ],
          travelMode: 'DRIVING',

        };

        directionsService.route(request1, function(result1, status1) {
          if (status1 == google.maps.DirectionsStatus.OK) {
            directionsDisplay1.setDirections(result1);
          }
        });



      

// function reducemap() {
//     document.getElementById("map-canvas").style.width = "620px";
//     google.maps.event.trigger( map, "resize" );
// }
// reducemap()

      // function toggleBounce() {
      //   if (marker.getAnimation() != null) {
      //     marker.setAnimation(null);
      //   } else {
      //     marker.setAnimation(google.maps.Animation.BOUNCE);
      //   }
      // }
      // toggleBounce()
      // google.maps.event.addDomListener(window, 'load', initialize);



  // var contentString = '<div class="iw-content">' + '<div class="iw-subTitle">My company </div>' + '<p>455 street</p>' + '<p>City, World</p>' + '<p>Canada, Postalcode</p>' + '</div>';
  // mapCenter=new google.maps.LatLng(50.645107,11.140137),
  // mapZoom= 3,

  // mapProp = {center:mapCenter,
  //   zoom:mapZoom,
  //    mapTypeId:google.maps.MapTypeId.ROADMAP}; 

  // map1 = new google.maps.Map(document.getElementById("map-canvas"),mapProp);
  var infowindow = new google.maps.InfoWindow({
  content:"Hello World!"
});




var icon = {
    url: "static/img/airplane9.png", // url
    scaledSize: new google.maps.Size(35, 35), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(17, 17), // anchor

    // color:new google.maps.("red") 
};


var marker = new google.maps.Marker({
  position:{lat: 34.2311317, lng:52.3777868},
  icon: icon,
  zIndex: 100
});
marker.setMap(map);

google.maps.event.addListener(marker, 'mouseover', (function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, "<p style='width:200px; length:200px' ><b>70 min</b> flight with Mahan air which is one of the best demostic airlines </p>", infowindow));


    google.maps.event.addListener(marker, 'mouseout', (function(marker, content, infowindow) {
      return function() {
        infowindow.close();
      };
    })(marker, "<p style='width:200px; length:200px' ><b>244 km</b> that we will travel with a luxury car or bus</p>", infowindow));


  // google.maps.event.addListener(map, 'click', function() {
  //   infowindow.close();
  // });

  // google.maps.event.addListener(infowindow, 'domready', function() {
 //    var iwOuter = $('.gm-style-iw');

 //    var iwBackground = iwOuter.prev();

 //    iwBackground.children(':nth-child(2)').css({
 //      'background': '#252525'});
    
 // var iwmain = iwBackground.children(':nth-child(2)');

 //    iwBackground.children(':nth-child(4)').css({
 //      'display': 'none'
 //    });

 //    var iwCloseBtn = iwOuter.next();

  // });


var icon = {
    url: "static/img/car2.png", // url
    scaledSize: new google.maps.Size(25, 25), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(12, 12), // anchor

    
};

 
var marker = new google.maps.Marker({
  position:{lat: 35.194181 , lng:51.0244323},
  icon: icon,
  zIndex: 100
});
marker.setMap(map);
google.maps.event.addListener(marker, 'mouseover', (function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, "<p style='width:200px; length:200px' ><b>244 km</b> We will wrap up our journey here </p>", infowindow));


    google.maps.event.addListener(marker, 'mouseout', (function(marker, content, infowindow) {
      return function() {
        infowindow.close();
      };
    })(marker, "<p style='width:200px; length:200px' ><b>244 km</b> that we will travel with a luxury car or bus</p>", infowindow));

var icon = {
    url: "static/img/car1.png", // url
    scaledSize: new google.maps.Size(25, 25), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(12, 12), // anchor

    
};

var marker = new google.maps.Marker({
  position:{lat: 33.664556 , lng:51.861235},
  icon: icon,
  zIndex: 100
});

marker.setMap(map);

google.maps.event.addListener(marker, 'mouseover', (function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, "<p style='width:200px; length:200px' ><b>216 km</b> We will continue our journey with some surprises . . .</p>", infowindow));


    google.maps.event.addListener(marker, 'mouseout', (function(marker, content, infowindow) {
      return function() {
        infowindow.close();
      };
    })(marker, "<p style='width:200px; length:200px' ><b>216 km</b> that we will travel with a luxury car or bus</p>", infowindow));




var marker = new google.maps.Marker({
  position:{lat: 31.463251 , lng:52.286350},
  icon: icon,
  zIndex: 100
});
marker.setMap(map);

google.maps.event.addListener(marker, 'mouseover', (function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, "<p style='width:200px; length:200px'; background: red ><b>483 km</b> that we will travel with a luxury car or bus. I cannot tell you exactly how long it would take because we will have a lot of fun!!</p>", infowindow));


    google.maps.event.addListener(marker, 'mouseout', (function(marker, content, infowindow) {
      return function() {
        infowindow.close();
      };
    })(marker, "<p style='width:200px; length:200px'; background: rgba(255, 255, 255, 1) ><b>483 km</b> that we will travel with a luxury car or bus</p>", infowindow));


function createMarker(latLng, text, motto, label, contentString) {

  var marker = new google.maps.Marker({
    position: latLng,
    map: map,
    label: {text: label, color: "white"}
  });
  google.maps.event.addListener(marker, "mouseover", function(evt) {
    var label = this.getLabel();
    label.color="black";
    this.setLabel(label);
  });
    google.maps.event.addListener(marker, "mouseout", function(evt) {
    var label = this.getLabel();
    label.color="white";
    this.setLabel(label);
  });

  var content = '<div class="iw-content" style="width:330px; length:330px">' + '<div class="iw-subTitle">'+ "<b>"+ text +"</b>" +' </div>' + '<p>'+ motto +' </p>' + '<p><img width="300px height="300px" src="static/img/'+label+'.jpg"></img></p>' + '</div>';
      var infowindow = new google.maps.InfoWindow({
    content: contentString
  });


// var content = 'address';

    var infowindow = new google.maps.InfoWindow()

    google.maps.event.addListener(marker, 'mouseover', (function(marker, content, infowindow) {
      return function() {
        infowindow.setContent(content);
        infowindow.open(map, marker);
      };
    })(marker, content, infowindow));
    google.maps.event.addListener(marker, 'mouseout', (function(marker, content, infowindow) {
      return function() {
        infowindow.close();
      };
    })(marker, content, infowindow));




// google.maps.event.addListener(marker, 'mouseover', function() {
//         // if( infowindow ) infowindow.close();
//     infowindow.open(map , marker);
//   });

//     google.maps.event.addListener(map, 'click', function() {
//     infowindow.close();
//   });
//  // marker.infowindow.close();
//       // google.maps.event.addListener(map, 'click', function() {
//       //               // infowindow.close();
//       //               // infowindow.setContent(contentString);
//       //               infowindow.open(map,marker);
//       //           });

//  google.maps.event.addListener(infowindow, 'domready', function() {
//     var iwOuter = $('.gm-style-iw');

//     var iwBackground = iwOuter.prev();

//     iwBackground.children(':nth-child(2)').css({
//       'background': '#252525'
//     });


//  var iwmain = iwBackground.children(':nth-child(2)');
//     iwBackground.children(':nth-child(4)').css({
//       'display': 'none'
//     });
// var iwCloseBtn = iwOuter.next();
//  });
//   // 
}

marker = createMarker({lat: 35.6899062, lng:51.307584}, "Tehran", 'We will arrive at Tehran and will stay for one night, and in the meantime we will visit some amazing places','A', 'AAA')
marker = createMarker({lat: 29.5460138, lng:52.5923618}, "Shiraz",  'We will stay on shiraz for a couple of days and will immense in civilization and love!','B', 'BBB')
marker = createMarker({lat: 32.6622111, lng:51.5469382}, "Isfahan",  'Isfahan, half of the world, is out third destination and will stay at Abbassi Hotel and also have incredible experience','C', 'CCC')
marker = createMarker({lat: 33.9814066, lng:51.3427133}, "Kashan",  'Last but not least, Kashan','D', 'DDD')

}





// marker.addListener('mouseover', function() {
//     infowindow.open(map, this);
// });

// // assuming you also want to hide the infowindow when user mouses-out
// marker.addListener('mouseout', function() {
//     infowindow.close();
// });




google.maps.event.addDomListener(window, 'load', initialize);