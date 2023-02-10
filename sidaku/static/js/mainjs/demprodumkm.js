
tambahdemprod   = document.getElementById("tambahdemprod")
editdemprod     = document.getElementById("editdemprod")
modaldemprod    = document.getElementById("modaldemprod")

nmprod          = document.getElementById("id_dpd_nmprod")
bulan           = document.getElementById("id_dpd_bulan")
tahun           = document.getElementById("id_dpd_tahun")
demand          = document.getElementById("id_dpd_demand")
produksi        = document.getElementById("id_dpd_produksi")

var strjson_demprod = []

modaldemprod.addEventListener("click", function(){

    nmprod.value = "";
    bulan.value = "";
    tahun.value = "";
    demand.value = "";
    produksi.value = "";

    $("#editdemprod").hide();
    $("#tambahdemprod").show();
});

tambahdemprod.addEventListener("click", function(){

    data = {
        "id":"",
        "dpd_nmprod":nmprod.value,
        "dpd_bulan":bulan.value,
        "dpd_tahun":tahun.value,
        "dpd_demand":demand.value,
        "dpd_produksi":produksi.value,
    }

    strjson_demprod.push(data);
    ConvertToTableDemprod();

    $("#demprod").text(JSON.stringify(strjson_demprod));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTableDemprod(index){
    strjson_demprod.splice(index,1);
    ConvertToTableDemprod();
    $("#demprod").text(JSON.stringify(strjson_demprod));
}


function EditTableDemprod(index){
    
    nmprod.value    = strjson_demprod[index].dpd_nmprod;
    bulan.value     = strjson_demprod[index].dpd_bulan;
    tahun.value     = strjson_demprod[index].dpd_tahun;
    demand.value    = strjson_demprod[index].dpd_demand;
    produksi.value  = strjson_demprod[index].dpd_produksi;

    idxinput.value = index;

    $("#editdemprod").show();
    $("#tambahdemprod").hide();
}


function EditDataDemprod(){

    idxinput = document.getElementById("idxinput");
    
    index = idxinput.value; 
    strjson_demprod[index].dpd_nmprod    = nmprod.value;
    strjson_demprod[index].dpd_bulan     = bulan.value ;
    strjson_demprod[index].dpd_tahun     = tahun.value  ;
    strjson_demprod[index].dpd_demand    = demand.value  ;
    strjson_demprod[index].dpd_produksi  = produksi.value    ;

    ConvertToTableDemprod();
    $("#jenprod").text(JSON.stringify(strjson_demprod));
}

function ConvertToTableDemprod(){
    html ="";
    for (let i = 0; i < strjson_demprod.length; i++) {
        html += "<tr>";
        html +=   "<td id='bulan-"+i+"'>"+ strjson_demprod[i].dpd_bulan+"</td>";
        html +=   "<td id='tahun-"+i+"'>"+ strjson_demprod[i].dpd_tahun+"</td>";
        html +=   "<td id='nmprod-"+i+"'>"+ strjson_demprod[i].dpd_nmprod+"</td>";
        html +=   "<td id='demand-"+i+"'>"+ strjson_demprod[i].dpd_demand+"</td>";
        html +=   "<td id='produksi-"+i+"'>"+ strjson_demprod[i].dpd_produksi+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#adddemprod' data-bs-whatever='Edit Data'  onclick='EditTableDemprod("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTableDemprod("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-demprod").html(html);
}