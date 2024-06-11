# Fetch

### Basic Fetch Without Async Code

This example demonstrates the basic usage of the Fetch API with promises:

```javascript
fetch('https://api.example.com/data')
  .then(function(response) {
    return response.json(); // Promise resolves with parsed JSON
  })
  .then(function(data) {
    console.log(data); // Promise resolves with data
  })
  .catch(function(error) {
    console.error('Error:', error); // Promise resolves with error
  });
```

### Explanation:

1. **`fetch('https://api.example.com/data')`**:
   - Initiates the fetch request and returns a promise.
2. **`then(function(response) { return response.json(); })`**:
   - The `fetch` promise resolves with a `response` object.
   - `response.json()` returns a promise that resolves with the parsed JSON data.
3. **`then(function(data) { console.log(data); })`**:
   - The JSON promise resolves with the `data`, which is logged to the console.
4. **`catch(function(error) { console.error('Error:', error); })`**:
   - If any promise in the chain is rejected, the `catch` block handles the error.

### Using Promises and Handling Resolutions:

When `fetch` is called, it returns a promise that resolves to a `Response` object. You handle this response by calling the `.then()` method, which also returns a promise. You can chain multiple `.then()` calls to handle each step of processing the response. If any of the promises are rejected (e.g., network error, failed JSON parsing), the `.catch()` method will handle the error.

### Example with Async/Await

Using async/await makes the code cleaner and easier to read:

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

### Explanation:

1. **`async function fetchData()`**:
   - Declares an asynchronous function.
2. **`const response = await fetch('https://api.example.com/data');`**:
   - Awaits the fetch request, which returns a `Response` object.
3. **`const data = await response.json();`**:
   - Awaits the parsing of the response JSON.
4. **`console.log(data);`**:
   - Logs the parsed data.
5. **`catch (error)`**:
   - Catches any errors that occur during the fetch or parsing.

By using async/await, the asynchronous code looks more like synchronous code, making it easier to read and maintain.