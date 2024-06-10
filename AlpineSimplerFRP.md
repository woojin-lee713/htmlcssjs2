## Alpine.js is built with the Proxy pattern

If you are interested in **[Design Pattern](https://www.geeksforgeeks.org/types-of-software-architecture-patterns/) architectures**, you may find it entertaining that in order to make the magic happen, the Alpine.reactive function makes use of the Proxy pattern.
A Proxy is basically a JavaScript object which allows you to wrap other objects, and to intercept and redefine operations on them. In a nutshell, Proxy objects make it possible to define objects that can be used in place of the original object, but which may redefine fundamental Object operations such as getting, setting, and defining properties, i.e., by using a little bit of Javascript in order to better understand that:

```javascript
let obj = { color: ‘blue’ }
let proxy = Alpine.reactive(obj)
```

Here, the function **Alpine.reactive receives a plain object and wraps it inside a Proxy object**. The “proxy” variable is a wrapper around the “obj” variable, so any attempts to get or set a “proxy” property will behave exactly as if you had interacted with “obj” directly:

```javascript
console.log(obj.color) // blue
console.log(proxy.color) // blue

proxy.color = ‘green’
 
console.log(obj.color) // green
```

Now, any time you update or retrieve a value from the proxy object, **Alpine is aware of this and can run any other logic** that depends on this data.

## Alpine.effect allows the creation of DOM reactivity via a jQuery-esque method

You can make powerful use of the second reactivity-maker function of Alpine – Alpine.reactive – which makes any data reactive. This works in combination with the previous reactivity maker:

```javascript
let obj = { color: ‘blue’ }
let proxy = Alpine.reactive(obj)
 
Alpine.effect(() => {
    console.log(proxy.color)
})
```

With this approach, the callback will be executed once, and whenever you interact with the reactive “color” property of the proxy object you will console.log its value.
This means you **can skip the Alpine-HTML template completely** and rely on vanilla Javascript DOM manipulations and the two Alpine reactivity-maker functions:

```javascript
let button = document.querySelector('button')
let span = document.querySelector('span')
 
let proxy = Alpine.reactive({ color: ‘blue’ })
 
Alpine.effect(() => {
    span.textContent = proxy.color
})
 
button.addEventListener('click', () => {
    proxy.color = (proxy.color == ‘blue’) ? ‘green’ : ‘blue’
}) 
```

