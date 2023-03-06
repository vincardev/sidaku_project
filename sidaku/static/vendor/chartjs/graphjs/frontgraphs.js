
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

getskalaumkm();
getomzetumkm();
getasetumkm();
getbidushumkm();

function getskalaumkm(){
    
    $.ajax({
        url: '/skalaumkm',
        type: 'GET',
        dataType: "json",
        
        success : function (resp) {
            var ctx = document.getElementById("pieSkala");
            var myPieChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ["Mikro", "Kecil", "Menengah"],
                datasets: [{
                data: [resp.sk_mikro.length, resp.sk_kecil.length, resp.sk_menengah.length],
                backgroundColor: ['#007bff', '#dc3545', '#28a745'],
                }],
            },
            options: {
                onClick:function(e){
                    var activePoints = myPieChart.getElementsAtEvent(e);
                    var selectedIndex = activePoints[0]._index;
                    
                    var modalGraph = document.getElementById('modalGraphSkl');
                    var modalTitle = modalGraph.querySelector('.modal-title');
                    // var modalBody = modalGraph.querySelector('.modal-body')
                    // var modalBodyInput = modalGraph.querySelector('.modal-body input')
                    respData ="";
                    if (selectedIndex == 0){
                        respData = resp.sk_mikro;
                        modalTitle.textContent = 'UMKM Skala Mikro';
                    } else if (selectedIndex == 1){
                        respData = resp.sk_kecil;
                        modalTitle.textContent = 'UMKM Skala Kecil';
                    } else if (selectedIndex == 2){
                        respData = resp.sk_menengah;
                        modalTitle.textContent = 'UMKM Skala Menengah';
                    } 

                    var content="";
                    content += '<div class="table-responsive">';
                    content += '<table class="table">';

                    content +=    
                        '<thead>' +
                            '<tr>' +
                            '<th>Nama Usaha</th>' +
                            '<th>Alamat Usaha</th>' +
                            '<th>Owner</th>' +
                            '<th>Omzet</th>' +
                            '<th>Total Aset</th>' +
                            '<th> </th>' +
                            '</tr>' +
                        '</thead>';
                    content += '<tbody>';

                    for (let i = 0; i < respData.length; i++) {
                        content += '<tr>'
                        content += '<td>'+respData[i].du_nmusha +'</td>';
                        content += '<td>'+respData[i].du_alusha +'</td>';
                        content += '<td>'+respData[i].pu_nmpmlk +'</td>';
                        content += '<td>'+formatNumber(respData[i].dtu_omzetthn) +'</td>';
                        content += '<td>'+formatNumber(respData[i].dtu_totalaset) +'</td>';
                        content += "<td><a href='umkm/"+ respData[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a></td>";

                        content += '</tr>'
                    }
                    content += '</tbody>';
                    content += '</table>';
                    content += '</div>';
                    
                    $('#graphContentSkl').html(content);
                    $('#modalGraphSkl').modal("show");

                    // alert(this.data.datasets[0].data[selectedIndex]);
                }
            },
            });

        },
        error: function(){
            alert('error');
        }
    });
}


function getomzetumkm(){
    
    $.ajax({
        url: '/highomzetumkm',
        type: 'GET',
        dataType: "json",
        
        success : function (resp) {
            respData = resp.high_omzukm;

            var label_arr = [];
            var highomz_arr = [];
              


            for (let i = 0; i < respData.length; i++) {
                label_arr.push(respData[i].du_nmusha);
                highomz_arr.push(respData[i].dtu_omzetthn);
            }

            var modalGraph = document.getElementById('modalGraphOmz');
            var modalTitle = modalGraph.querySelector('.modal-title');

            modalTitle.textContent = '10 UMKM Omzet Tertinggi';

            var content="";
            content += '<div class="table-responsive">';
            content += '<table class="table">';

            content +=    
                '<thead>' +
                    '<tr>' +
                    '<th>Nama Usaha</th>' +
                    '<th>Alamat Usaha</th>' +
                    '<th>Owner</th>' +
                    '<th>Omzet</th>' +
                    // '<th>Total Aset</th>' +
                    '<th> </th>' +
                    '</tr>' +
                '</thead>';
            content += '<tbody>';

            for (let i = 0; i < respData.length; i++) {
                content += '<tr>'
                content += '<td>'+respData[i].du_nmusha +'</td>';
                content += '<td>'+respData[i].du_alusha +'</td>';
                content += '<td>'+respData[i].pu_nmpmlk +'</td>';
                content += '<td>'+formatNumber(respData[i].dtu_omzetthn) +'</td>';
                // content += '<td>'+formatNumber(respData[i].dtu_totalaset) +'</td>';
                content += "<td><a href='umkm/"+ respData[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a></td>";

                content += '</tr>'
            }
            content += '</tbody>';
            content += '</table>';
            content += '</div>';

            $('#graphContentOmz').html(content);


            var ctx = document.getElementById("barOmzetChart");
            var myLineChart1 = new Chart(ctx, {
              type: 'bar',
              data: {
                labels: label_arr,
                datasets: [{
                  label: "Omzet",
                  backgroundColor: "rgba(2,117,216,1)",
                  borderColor: "rgba(2,117,216,1)",
                  data: highomz_arr,
                }],
              },
              options: {
                scales: {
                  xAxes: [{
                    time: {
                      unit: 'Nama Usaha'
                    },
                    gridLines: {
                      display: false
                    },
                    ticks: {
                      maxTicksLimit: 10
                    }
                  }],
                  yAxes: [{
                    ticks: {
                    //   min: 0,
                    //   max: 1000000000,
                      maxTicksLimit: 10
                    },
                    gridLines: {
                      display: true
                    }
                  }],
                },
                legend: {
                  display: false
                },
                onClick:function(e){

                    // var activePoints = myLineChart1.getElementsAtEvent(e);
                    // var selectedIndex = activePoints[0]._index;
                    
                   
                    $('#modalGraphOmz').modal("show");


                    // alert(this.data.datasets[0].data[selectedIndex]);
                }

              }
            });

        },
        error: function(){
            alert('error');
        }
    });
}

function getasetumkm(){
    
    $.ajax({
        url: '/highasetumkm',
        type: 'GET',
        dataType: "json",
        
        success : function (resp) {
            respData = resp.high_astumkm;

            var label_arr = [];
            var highaset_arr = [];
              


            for (let i = 0; i < respData.length; i++) {
                label_arr.push(respData[i].du_nmusha);
                highaset_arr.push(respData[i].dtu_totalaset);
            }


            var modalGraph = document.getElementById('modalGraphAst');
            var modalTitle = modalGraph.querySelector('.modal-title');

            modalTitle.textContent = '10 UMKM Investasi Tertinggi';

            var content="";
            content += '<div class="table-responsive">';
            content += '<table class="table">';

            content +=    
                '<thead>' +
                    '<tr>' +
                    '<th>Nama Usaha</th>' +
                    '<th>Alamat Usaha</th>' +
                    '<th>Owner</th>' +
                    // '<th>Omzet</th>' +
                    '<th>Total Aset</th>' +
                    '<th> </th>' +
                    '</tr>' +
                '</thead>';
            content += '<tbody>';

            for (let i = 0; i < respData.length; i++) {
                content += '<tr>'
                content += '<td>'+respData[i].du_nmusha +'</td>';
                content += '<td>'+respData[i].du_alusha +'</td>';
                content += '<td>'+respData[i].pu_nmpmlk +'</td>';
                // content += '<td>'+formatNumber(respData[i].dtu_omzetthn) +'</td>';
                content += '<td>'+formatNumber(respData[i].dtu_totalaset) +'</td>';
                content += "<td><a href='umkm/"+ respData[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a></td>";

                content += '</tr>'
            }
            content += '</tbody>';
            content += '</table>';
            content += '</div>';
            
            $('#graphContentAst').html(content);



            var ctx = document.getElementById("barAsetChart");
            var myLineChart2 = new Chart(ctx, {
              type: 'bar',
              data: {
                labels: label_arr,
                datasets: [{
                  label: "Aset",
                  backgroundColor: "rgba(2,117,216,1)",
                  borderColor: "rgba(2,117,216,1)",
                  data: highaset_arr,
                }],
              },
              options: {
                scales: {
                  xAxes: [{
                    time: {
                      unit: 'Nama Usaha'
                    },
                    gridLines: {
                      display: false
                    },
                    ticks: {
                      maxTicksLimit: 10
                    }
                  }],
                  yAxes: [{
                    ticks: {
                    //   min: 0,
                    //   max: 1000000000,
                      maxTicksLimit: 10
                    },
                    gridLines: {
                      display: true
                    }
                  }],
                },
                legend: {
                  display: false
                },
                onClick:function(e){
                    // var activePoints = myLineChart2.getElementsAtEvent(e);
                    // var selectedIndex = activePoints[0]._index;
                    
                    $('#modalGraphAst').modal("show");

                    // alert(this.data.datasets[0].data[selectedIndex]);
                }

              }
            });

        },
        error: function(){
            alert('error');
        }
    });
}

function getbidushumkm(){
    
  $.ajax({
      url: '/bidangusahaumkm',
      type: 'GET',
      dataType: "json",
      
      success : function (resp) {
      
        var label_arr = [];
        var totalumkm_arr = [];
          
        // console.log (resp.bidush_umkm);
        // console.log (resp.umkm_data);

        for (let i = 0; i < resp.bidush_umkm.length; i++) {
            label_arr.push(resp.bidush_umkm[i].nama);
            // totalumkm_arr.push(respData[i].dtu_totalaset);
        }
        for (let i = 0; i < resp.umkm_data.length; i++) {
          console.log(resp.umkm_data[i].du_bdgusha);
            // label_arr.push(resp.bidush_umkm[i].nama);
            // totalumkm_arr.push(respData[i].dtu_totalaset);
        }

      
        // var ctx = document.getElementById("pieBidush");
        //   var myPieChart = new Chart(ctx, {
        //   type: 'pie',
        //   data: {
        //       labels: ["Mikro", "Kecil", "Menengah"],
        //       datasets: [{
        //       data: [resp.sk_mikro.length, resp.sk_kecil.length, resp.sk_menengah.length],
        //       backgroundColor: ['#007bff', '#dc3545', '#28a745'],
        //       }],
        //   },
        //   options: {
        //       onClick:function(e){
        //           var activePoints = myPieChart.getElementsAtEvent(e);
        //           var selectedIndex = activePoints[0]._index;
                  
        //           var modalGraph = document.getElementById('modalGraphSkl');
        //           var modalTitle = modalGraph.querySelector('.modal-title');
        //           // var modalBody = modalGraph.querySelector('.modal-body')
        //           // var modalBodyInput = modalGraph.querySelector('.modal-body input')
        //           respData ="";
        //           if (selectedIndex == 0){
        //               respData = resp.sk_mikro;
        //               modalTitle.textContent = 'UMKM Skala Mikro';
        //           } else if (selectedIndex == 1){
        //               respData = resp.sk_kecil;
        //               modalTitle.textContent = 'UMKM Skala Kecil';
        //           } else if (selectedIndex == 2){
        //               respData = resp.sk_menengah;
        //               modalTitle.textContent = 'UMKM Skala Menengah';
        //           } 

        //           var content="";
        //           content += '<div class="table-responsive">';
        //           content += '<table class="table">';

        //           content +=    
        //               '<thead>' +
        //                   '<tr>' +
        //                   '<th>Nama Usaha</th>' +
        //                   '<th>Alamat Usaha</th>' +
        //                   '<th>Owner</th>' +
        //                   '<th>Omzet</th>' +
        //                   '<th>Total Aset</th>' +
        //                   '<th> </th>' +
        //                   '</tr>' +
        //               '</thead>';
        //           content += '<tbody>';

        //           for (let i = 0; i < respData.length; i++) {
        //               content += '<tr>'
        //               content += '<td>'+respData[i].du_nmusha +'</td>';
        //               content += '<td>'+respData[i].du_alusha +'</td>';
        //               content += '<td>'+respData[i].pu_nmpmlk +'</td>';
        //               content += '<td>'+formatNumber(respData[i].dtu_omzetthn) +'</td>';
        //               content += '<td>'+formatNumber(respData[i].dtu_totalaset) +'</td>';
        //               content += "<td><a href='umkm/"+ respData[i].id +"'  class='btn btn-sm btn-success rounded-0 text-white w-100 '>Detail</a></td>";

        //               content += '</tr>'
        //           }
        //           content += '</tbody>';
        //           content += '</table>';
        //           content += '</div>';
                  
        //           $('#graphContentSkl').html(content);
        //           $('#modalGraphSkl').modal("show");

        //           // alert(this.data.datasets[0].data[selectedIndex]);
        //       }
        //   },
        //   });

      },
      error: function(){
          alert('error');
      }
  });
}


function formatNumber(num) {
    if (num == null){
        return 0;
    } else {
        return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.');
    }
}