   function debug() {
        var reg_url = $("#reg_url").val();
        var req_method = $('input:radio[name="req_method"]:checked').val();
        var reg_header =$("#reg_header").val();
        var req_type =$('input:radio[name="req_type"]:checked').val();
        var reg_param =$("#reg_param").val();

        if(reg_url == ""){
            alert("请求的url不能为空！")
            $("#reg_url").focus()
            return;
        }

        $.ajax({
            type:"POST",
            url:'/case/debug/',
            data:{
                reg_url:reg_url,
                req_method:req_method,
                reg_header:reg_header,
                req_type:req_type,
                reg_param:reg_param
            },
            success:function (result) {

                $("#req_result").val(result);

            }
        });

    };


    function req_assert() {
        var req_assert_type = $('input:radio[name="req_assert_type"]:checked').val();
        var req_assert_param =$("#req_assert_param").val();
        var req_result =$("#req_result").val();

        if(req_assert_param == ""){
            alert("断言的预期结果不能为空！")
            $("#req_assert_param").focus()
            return;
        }

        if(req_result == ""){
            alert("断言的实际结果不能为空！")
            $("#req_result").focus()
            return;
        }

        $.ajax({
            type:"POST",
            url:'/case/req_assert/',
            data:{
                req_assert_type:req_assert_type,
                req_assert_param:req_assert_param,
                req_result:req_result,
            },
            success:function (result) {

                alert(result)

            }
        });

    };

    function queryModule() {


        var req_project = $("#req_project option:selected").val();

        if(req_project == ""){

            $("#req_module").empty()

            $("#req_module").append("<option value='请选择'>请选择</option>");

            return;
        }

        $.ajax({
            type:"GET",
            url:'/case/queryModule/',
            data:{
                req_project:req_project
            },
            success:function (result) {

                var res = JSON.parse(result)

                $("#req_module").empty()

                $("#req_module").append("<option value='请选择'>请选择</option>");

                Object.keys(res).forEach(function (key) {
                    $("#req_module").append("<option value='"+key+"'>"+res[key]+"</option>");
                    
                })


            }
        });


    }
