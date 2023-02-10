
tambahdemsupp   = document.getElementById("tambahdemsupp")
editdemsupp     = document.getElementById("editdemsupp")
modaldemsupp    = document.getElementById("modaldemsupp")

jensupdsp          = document.getElementById("id_dsp_jensup")
bulandsp           = document.getElementById("id_dsp_bulan")
tahundsp           = document.getElementById("id_dsp_tahun")
demanddsp          = document.getElementById("id_dsp_demand")
produksidsp        = document.getElementById("id_dsp_produksi")

var strjson_demsupp = []

modaldemsupp.addEventListener("click", function(){

    jensupdsp.value = "";
    bulandsp.value = "";
    tahundsp.value = "";
    demanddsp.value = "";
    produksidsp.value = "";

    $("#editdemsupp").hide();
    $("#tambahdemsupp").show();
});

tambahdemsupp.addEventListener("click", function(){

    data = {
        "id":"",
        "dsp_jensup":jensupdsp.value,
        "dsp_bulan":bulandsp.value,
        "dsp_tahun":tahundsp.value,
        "dsp_demand":demanddsp.value,
        "dsp_produksi":produksidsp.value,
    }

    strjson_demsupp.push(data);
    ConvertToTableDemsupp();

    $("#demsupp").text(JSON.stringify(strjson_demsupp));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTableDemsupp(index){
    strjson_demsupp.splice(index,1);
    ConvertToTableDemsupp();
    $("#demsupp").text(JSON.stringify(strjson_demsupp));
}


function EditTableDemsupp(index){
    
    jensupdsp.value    = strjson_demsupp[index].dsp_jensup;
    bulandsp.value     = strjson_demsupp[index].dsp_bulan;
    tahundsp.value     = strjson_demsupp[index].dsp_tahun;
    demanddsp.value    = strjson_demsupp[index].dsp_demand;
    produksidsp.value  = strjson_demsupp[index].dsp_produksi;

    idxinput.value = index;

    $("#editdemsupp").show();
    $("#tambahdemsupp").hide();
}


function EditDataDemsupp(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_demsupp[index].dsp_jensup    = jensupdsp.value;
    strjson_demsupp[index].dsp_bulan     = bulandsp.value ;
    strjson_demsupp[index].dsp_tahun     = tahundsp.value  ;
    strjson_demsupp[index].dsp_demand    = demanddsp.value  ;
    strjson_demsupp[index].dsp_produksi  = produksidsp.value    ;

    ConvertToTableDemsupp();
    $("#jensupp").text(JSON.stringify(strjson_demsupp));
}

function ConvertToTableDemsupp(){
    html ="";
    for (let i = 0; i < strjson_demsupp.length; i++) {
        html += "<tr>";
        html +=   "<td id='bulandsp-"+i+"'>"+ strjson_demsupp[i].dsp_bulan+"</td>";
        html +=   "<td id='tahundsp-"+i+"'>"+ strjson_demsupp[i].dsp_tahun+"</td>";
        html +=   "<td id='jensupdsp-"+i+"'>"+ strjson_demsupp[i].dsp_jensup+"</td>";
        html +=   "<td id='demanddsp-"+i+"'>"+ strjson_demsupp[i].dsp_demand+"</td>";
        html +=   "<td id='produksidsp-"+i+"'>"+ strjson_demsupp[i].dsp_produksi+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#adddemsupp' data-bs-whatever='Edit Data'  onclick='EditTableDemsupp("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTableDemsupp("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-demsupp").html(html);
}