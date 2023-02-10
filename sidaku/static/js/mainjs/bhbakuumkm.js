
tambahbhbaku   = document.getElementById("tambahbhbaku")
editbhbaku     = document.getElementById("editbhbaku")
modalbhbaku    = document.getElementById("modalbhbaku")

jenbhbaku       = document.getElementById("id_jen_bhbaku")
volumebb        = document.getElementById("id_volumebb")
nilaibb         = document.getElementById("id_nilai")
asalBB          = document.getElementById("id_asalBB")

var strjson_bhbaku = []

modalbhbaku.addEventListener("click", function(){

    jenbhbaku.value = "";
    volumebb.value = "";
    nilaibb.value = "";
    asalBB.value = "";

    $("#editbhbaku").hide();
    $("#tambahbhbaku").show();
});

tambahbhbaku.addEventListener("click", function(){

    data = {
        "id":"",
        "jen_bhbaku":jenbhbaku.value,
        "volume":volumebb.value,
        "nilai":nilaibb.value,
        "asalBB":asalBB.value,
    }

    strjson_bhbaku.push(data);
    ConvertToTablebhbaku();

    $("#databhbaku").text(JSON.stringify(strjson_bhbaku));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTablebhbaku(index){
    strjson_bhbaku.splice(index,1);
    ConvertToTablebhbaku();
    $("#databhbaku").text(JSON.stringify(strjson_bhbaku));
}


function EditTablebhbaku(index){
    
    jenbhbaku.value     = strjson_bhbaku[index].jen_bhbaku;
    volumebb.value      = strjson_bhbaku[index].volume;
    nilaibb.value       = strjson_bhbaku[index].nilai;
    asalBB.value        = strjson_bhbaku[index].asalBB;

    idxinput.value = index;

    $("#editbhbaku").show();
    $("#tambahbhbaku").hide();
}


function EditDatabhbaku(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_bhbaku[index].jen_bhbaku    = jenbhbaku.value;
    strjson_bhbaku[index].volume        = volumebb.value ;
    strjson_bhbaku[index].nilai         = nilaibb.value  ;
    strjson_bhbaku[index].asalBB        = asalBB.value  ;

    ConvertToTablebhbaku();
    $("#databhbaku").text(JSON.stringify(strjson_bhbaku));
}

function ConvertToTablebhbaku(){
    html ="";
    for (let i = 0; i < strjson_bhbaku.length; i++) {
        html += "<tr>";
        html +=   "<td id='jen_bhbaku-"+i+"'>"+ strjson_bhbaku[i].jen_bhbaku+"</td>";
        html +=   "<td id='volume-"+i+"'>"+ strjson_bhbaku[i].volume+"</td>";
        html +=   "<td id='nilai-"+i+"'>"+ strjson_bhbaku[i].nilai+"</td>";
        html +=   "<td id='asalBB-"+i+"'>"+ strjson_bhbaku[i].asalBB+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addbhbaku' data-bs-whatever='Edit Data'  onclick='EditTablebhbaku("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTablebhbaku("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-bhbaku").html(html);
}