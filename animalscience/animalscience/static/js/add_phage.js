function showDuplicates(){
    
    var form = $('#addPhageForm')[0];      //Without [0] => its a list
    var formData = new FormData(form);
    formData.append('flag',1);
    
    $.ajax({
        url:'/add_phage/',
        data: formData,
        type: 'post',
        dataType:'json',
        contentType:false,
        processData:false,
        success: function (data){
            if ((data.approvePhage == 0) || (data.approveCPTid == 0)){
                
                var s="";
                
                if(data.approvePhage == 0){
                    //display duplicate phages
                    var obj1 = JSON.parse(data.duplicatePhagesPhages);
                    var obj2 = JSON.parse(data.duplicatePhagesCPTid);
                    var n1=obj1.length;
                    
                    s = s + "Phages with the following Phage Names already exist:\n";
                    s = s + "Phage Name         CPT ID\n";
                    
                    s = s + "\n";
                    
                    for(i=0; i<n1; ++i){
                        s = s + obj1[i] + "         " + obj2[i] + "\n";
                    }
                }
                
                if (data.approvePhage == 0 && data.approvePhage == 0){
                    s = s+"\n\n";
                }
                
                 if(data.approveCPTid == 0){
                    var obj3 = JSON.parse(data.duplicateCPTidPhages);
                    var obj4 = JSON.parse(data.duplicateCPTidCPTid);
                    var n2=obj3.length;
                    
                    s = s + "Phages with the following CPT IDs already exist:\n";
                    s = s + "Phage Name         CPT ID\n";
                    
                    s = s + "\n";
                    
                    for(i=0; i<n2; ++i){
                        s = s + obj3[i] + "         " + obj4[i] + "\n";
                    }
                }
                
                s += "To overwrite the existing phages, please go to Edit Phage section !";
                
                alert(s);
                
            } else {
                window.location='/view_phages/';       //?add_status=true
            }
            
        }
    });
    return false;
}

function RedirectToPage()
  {
      window.location='/view_phages/';
  }