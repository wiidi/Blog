function show() {
				var box = document.querySelector('.box');
				var text = box.innerHTML;
				var newBox = document.createElement("div");
				var btn = document.createElement("a");
				newBox.innerHTML = text.substring(0, 100);
				btn.innerHTML = text.length > 100 ? "详情" : "";
				btn.href = "###";
				btn.onclick = function() {
					if(btn.innerHTML == "详情") {
						btn.innerHTML = "收起";
						newBox.innerHTML = text;
					} else {
						btn.innerHTML = "详情";
						newBox.innerHTML = text.substring(0, 100);
					}
				}
				box.innerHTML = "";
				box.appendChild(newBox);
				box.appendChild(btn);
			}
			window.onload = function() {
				show();
			}