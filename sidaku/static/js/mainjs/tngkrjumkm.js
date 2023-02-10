
tambahtngkrj   = document.getElementById("tambahtngkrj")
edittngkrj     = document.getElementById("edittngkrj")
modaltngkrj    = document.getElementById("modaltngkrj")

jnstngkrj       = document.getElementById("id_jenis_tngkrj")
jmlorg          = document.getElementById("id_jml_org")
pendidikan      = document.getElementById("id_pendidikan")

var strjson_tngkrj = []

modaltngkrj.addEventListener("click", function(){

    jnstngkrj.value = "";
    jmlorg.value = "";
    pendidikan.value = "";

    $("#edittngkrj").hide();
    $("#tambahtngkrj").show();
});

tambahtngkrj.addEventListener("click", function(){

    data = {
        "id":"",
        "jenis_tngkrj":jnstngkrj.value,
        "jml_org":jmlorg.value,
        "pendidikan":pendidikan.value,
    }

    strjson_tngkrj.push(data);
    ConvertToTableTngkrj();

    $("#tngkrj").text(JSON.stringify(strjson_tngkrj));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTableTngkrj(index){
    strjson_tngkrj.splice(index,1);
    ConvertToTableTngkrj();
    $("#tngkrj").text(JSON.stringify(strjson_tngkrj));
}


function EditTableTngkrj(index){
    
    jnstngkrj.value    = strjson_tngkrj[index].jenis_tngkrj;
    jmlorg.value  = strjson_tngkrj[index].jml_org;
    pendidikan.value     = strjson_tngkrj[index].pendidikan;

    idxinput.value = index;

    $("#edittngkrj").show();
    $("#tambahtngkrj").hide();
}


function EditDataTngkrj(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_tngkrj[index].jenis_tngkrj      = jnstngkrj.value;
    strjson_tngkrj[index].jml_org     = jmlorg.value ;
    strjson_tngkrj[index].pendidikan   = pendidikan.value  ;

    ConvertToTableTngkrj();
    $("#tngkrj").text(JSON.stringify(strjson_tngkrj));
}

function ConvertToTableTngkrj(){
    html ="";
    for (let i = 0; i < strjson_tngkrj.length; i++) {
        html += "<tr>";
        html +=   "<td id='jenis_tngkrj-"+i+"'>"+ strjson_tngkrj[i].jenis_tngkrj+"</td>";
        html +=   "<td id='jml_org-"+i+"'>"+ strjson_tngkrj[i].jml_org+"</td>";
        html +=   "<td id='pendidikan-"+i+"'>"+ strjson_tngkrj[i].pendidikan+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addtngkrj' data-bs-whatever='Edit Data'  onclick='EditTableTngkrj("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTableTngkrj("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-tngkrj").html(html);
}