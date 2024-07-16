$(document).ready(function(){
    $(".upload_photo").on("click", function(e){
      $("#id_profile_photo").click();
    });
    
    $("#id_profile_photo").on("change", function(e){
      var reader = new FileReader();
      reader.onload = function(e) {
        $('.upload_photo').html('<img src="'+e.target.result+'" alt="Profile Photo" class="img-fluid rounded-circle" style="width: 100%; height: 100%;">');
      }
      reader.readAsDataURL(this.files[0]);
    });

  })