/**
 * Created by Administrator on 2017/9/4 0004.
 */
(function($){
    $.fn.textSearch = function(str,options){
        var defaults = {
            divFlag: true,
            divStr: " ",
            markClass: "",
            markColor: "#99bac6",
            nullReport: true,
            callback: function(){
                return false;
            }
        };
        var sets = $.extend({}, defaults, options || {}), clStr;
        if(sets.markClass){
            clStr = "class='"+sets.markClass+"'";
        }else{
            clStr = "style='background-color:"+sets.markColor+";'";
        }

        //对前一次高亮处理的文字还原
        $("span[rel='mark']").removeAttr("class").removeAttr("style").removeAttr("rel");


        //字符串正则表达式关键字转化
        $.regTrim = function(s){
            var imp = /[\^\.\\\|\(\)\*\+\-\$\[\]\?]/g;
            var imp_c = {};
            imp_c["^"] = "\\^";
            imp_c["."] = "\\.";
            imp_c["\\"] = "\\\\";
            imp_c["|"] = "\\|";
            imp_c["("] = "\\(";
            imp_c[")"] = "\\)";
            imp_c["*"] = "\\*";
            imp_c["+"] = "\\+";
            imp_c["-"] = "\\-";
            imp_c["$"] = "\$";
            imp_c["["] = "\\[";
            imp_c["]"] = "\\]";
            imp_c["?"] = "\\?";
            s = s.replace(imp,function(o){
                return imp_c[o];
            });
            return s;
        };
        $(this).each(function(){
            var t = $(this);
            str = $.trim(str);
            if(str === ""){
                return false;
            }else{
                //将关键字push到数组之中
                var arr = [];
                if(sets.divFlag){
                    arr = str.split(sets.divStr);
                }else{
                    arr.push(str);
                }
            }
            var v_html = t.html();
            //删除注释
            v_html = v_html.replace(/<!--(?:.*)\-->/g,"");

            //将HTML代码支离为HTML片段和文字片段，其中文字片段用于正则替换处理，而HTML片段置之不理
            var tags = /[^<>]+|<(\/?)([A-Za-z]+)([^<>]*)>/g;
            var a = v_html.match(tags), test = 0;
            $.each(a, function(i, c){
                if(!/<(?:.|\s)*?>/.test(c)){//非标签
                    //开始执行替换
                    $.each(arr,function(index, con){
                        if(con === ""){return;}
                        var reg = new RegExp($.regTrim(con), "g");
                        if(reg.test(c)){
                            //正则替换
                            c = c.replace(reg,"♂"+con+"♀");
                            test = 1;
                        }
                    });
                    c = c.replace(/♂/g,"<span rel='mark' "+clStr+">").replace(/♀/g,"</span>");
                    a[i] = c;
                }
            });
            //将支离数组重新组成字符串
            var new_html = a.join("");

            $(this).html(new_html);

            if(test === 0 && sets.nullReport){
                alert("没有搜索结果");
                return false;
            }

            //执行回调函数
            sets.callback();
        });
    };
})(jQuery);

/**
 * usage
 * ```
 * ret=parseMarkDown(str)
 * console.log(ret)
 * ```
 * @param str
 * @returns {string|XML|*}
 */
function parseMarkDown(str) {
    str=str.replace(/-|#|> |~|\*|`/g,"");
    str=str.replace(/[\[]+[^\]]*[\]]+[^\n]*/g,"");
    str=str.replace(/\u0021\[]+[(]*[^)]+[)]/g,"");
    str=str.replace(/\r/g,"");
    str=str.replace(/\n\n/g,"\n");
    return str;
}

Function.prototype.getMultilines = function () {
    var lines = String(this);
    lines = lines.substring(lines.indexOf("/*")+3, lines.lastIndexOf("*/"));
    return lines;
};
var lines = function(){
    /*
     ---
     > ~~简书居然没有官方 Markdown 教程，我来~~

     首先，“Markdown 其实很简单。在简书上学习 Markdown 最方便。”

     [official_md_guide]: http://jianshu.io/p/q81RER

     ---
     # 1. 标题

     为了获得上面的 “`1. 标题`”， 在 Markdown 编辑器里输入：

     ~~~
     # 1. 标题
     ~~~

     “`#`” 后最好加个空格。除此之外，还有 5 级标题，依次有不同的字体大小，即

     ~~~
     ## 二级标题
     ### 三级标题
     #### 四级标题
     ##### 五级标题
     ###### 六级标题
     ~~~

     这样就有：

     ## 二级标题
     ### 三级标题
     #### 四级标题
     ##### 五级标题
     ###### 六级标题


     */
};