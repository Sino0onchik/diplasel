var g=(e,n,t)=>new Promise((r,o)=>{var c=a=>{try{i(t.next(a))}catch(u){o(u)}},s=a=>{try{i(t.throw(a))}catch(u){o(u)}},i=a=>a.done?r(a.value):Promise.resolve(a.value).then(c,s);i((t=t.apply(e,n)).next())});function h(e){var n=[],t="";for(t in e)n.push(t);return n}function d(e){return e=JSON.stringify(e),!(typeof e!="string"||!/^\{[\s\S]*\}$/.test(e))}function y(e){return e instanceof Array}function m(e){return Array.prototype.slice.call(e)}function f(){if(!(this instanceof f))return new f}f.prototype={get:function(e){for(var n=e+"=",t=document.cookie.split(";"),r=0;r<t.length;r++){for(var o=t[r];o.charAt(0)==" ";)o=o.substring(1,o.length);if(o.indexOf(n)==0)return decodeURI(o.substring(n.length,o.length))}return!1},set:function(e,n,t){if(d(e))for(const r in e)this.set(r,e[r],n,t);else if(typeof e=="string"){const r=d(t)?t:{expires:t},o=r.path!==void 0?`;path=${r.path};path=/`:";path=/",c=r.domain?`;domain=${r.domain}`:"",s=r.secure?";secure":"";let i=r.expires!==void 0?r.expires:"";typeof i=="string"&&i!==""?i=new Date(i):typeof i=="number"&&(i=new Date(+new Date+1e3*60*60*24*i)),i!==""&&"toGMTString"in i&&(i=`;expires=${i.toGMTString()}`);const a=r.sameSite?`;SameSite=${r.sameSite}`:"";document.cookie=`${e}=${encodeURI(n)+i+o+c+s+a}`}},remove:function(e){e=y(e)?e:m(arguments);for(var n=0,t=e.length;n<t;n++)this.set(e[n],"",-1);return e},clear:function(e){return e?this.remove(e):this.remove(h(this.all()))},all:function(){if(document.cookie==="")return{};for(var e=document.cookie.split("; "),n={},t=0,r=e.length;t<r;t++){var o=e[t].split("=");n[decodeURI(o[0])]=decodeURI(o[1])}return n}};let l=null;const p=function(e,n,t){const r=arguments;if(l||(l=f()),r.length===0)return l.all();if(r.length===1&&e===null)return l.clear();if(r.length===2&&!n)return l.clear(e);if(typeof e=="string"&&!n)return l.get(e);if(typeof e=="string"&&n||d(e))return l.set(e,n,t)};for(const e in f.prototype)p[e]=f.prototype[e];const v=document.getElementById("csrfCookieName").value,k=document.getElementById("csrfTokenInDOM").value==="True";function S(){if(k){let e=document.querySelector('input[name="csrfmiddlewaretoken"]');return e?e.value:null}return p.get(v)}function T(){return g(this,null,function*(){let e=this.dataset.id,n=this.dataset.url;try{let o=(yield(yield fetch(n,{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":S()},body:JSON.stringify({})})).json()).is_favorite,c=`.query_favorite_toggle[data-id='${e}']`,s=document.querySelector(c);s&&(o?(s.classList.remove("bi-heart"),s.classList.add("bi-heart-fill")):(s.classList.remove("bi-heart-fill"),s.classList.add("bi-heart")))}catch(t){console.error("Error:",t),alert("error")}})}export{p as c,S as g,T as t};
