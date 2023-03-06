
var marker_koperasi = [];
var marker_umkm = [];
var LatitDef = -7.8751223;
var LongiDef = 112.5109015;
var map_init = L.map('maparea',{
    renderer:  L.canvas({ padding: 0.5 })
}).setView([LatitDef, LongiDef], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { 
    scrollWheelZoom: true,
    maxZoom: 19,
    // attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map_init);


// map.scrollWheelZoom.disable();

// var urlstring = "{% url 'home:allmap' %}";
getadat();
function getadat(){


    var umkmIcon = new L.Icon({
        iconUrl: 'static/icon/markers/marker-icon-2x-red.png',
        shadowUrl: 'static/icon/markers/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    var kopIcon = new L.Icon({
        iconUrl: 'static/icon/markers/marker-icon-2x-green.png',
        shadowUrl: 'static/icon/markers/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    $.ajax({
        url: '/allmap',
        // url: '/allmap/kab/' + kabid +'/'+briid,
        // url: urlstring,
        type: 'GET',
        dataType: "json",
    
        success : function (resp) {
            for (let i = 0; i < resp.koperasi.length; i++) {

                var lat = resp.koperasi[i].rkp_lat;
                var lng = resp.koperasi[i].rkp_long;
                var imgsrc = resp.koperasi[i].du_ftkop;

                if (lat != null && lng != null){

                    if (!imgsrc)
                        imgsrc='default/no_image.jpg';
                
                    var content="";
                    content += "<div class='card'  style='width: 13rem;' >";
                    content += "<img src='media/"+imgsrc+"' class='card-img-top' style='max-height:120px;object-fit:cover;'>";
                    content += "<div class='card-body'>";
                    content += "<h5 class='card-title'>"+ resp.koperasi[i].du_nakop +"</h5>";
                    content += "<p class='card-text'>"+resp.koperasi[i].du_alkop+"</p>";
                    content += "<a href='koperasi/"+ resp.koperasi[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a>";
                    content += "</div>";
                                // form.intance.du_ftkop.url
                                // content += "</div>";

                    var newmarker = new L.marker([lat,lng],{icon:kopIcon}).addTo(map_init)
                    .bindPopup(content ).openPopup();
                    marker_koperasi.push(newmarker);

                    map_init.setView([lat,lng]);
                }

              }
              
            for (let i = 0; i < resp.umkmdata.length; i++) {

                var lat = resp.umkmdata[i].du_lat;
                var lng = resp.umkmdata[i].du_long;
                var imgsrc = resp.umkmdata[i].du_ftusha;


                if (lat != null && lng != null){

                    if (!imgsrc)
                        imgsrc='default/no_image.jpg';
                    
                    var content="";
                    content += "<div class='card'  style='width: 13rem;' >";
                    content += "<img src='media/"+imgsrc+"' class='card-img-top' style='max-height:120px;object-fit:cover;'>";
                    content += "<div class='card-body'>";
                    content += "<h5 class='card-title'>"+ resp.umkmdata[i].du_nmusha +"</h5>";
                    content += "<p class='card-text'>"+resp.umkmdata[i].du_alusha+"</p>";
                    content += "<a href='umkm/"+ resp.umkmdata[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a>";
                    content += "</div>";
                                // form.intance.du_ftkop.url
                                // content += "</div>";

                    var newmarker = new L.marker([lat,lng],{icon:umkmIcon}).addTo(map_init)
                    .bindPopup(content ).openPopup();
                    marker_umkm.push(newmarker);

                    map_init.setView([lat,lng]);
                }
            }
    
        },
        error: function(){
        }
    });
}
