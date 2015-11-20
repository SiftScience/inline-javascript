# Inline Javascript Demo

Simple web server demonstrates how to run Sift Science Javascript integration locally
embedded within each page (rather than by fetching the code from the Sift Science CDN).

```bash
$ BEACON_HOST=//my-beacon-host.com BEACON_KEY=my_beacon_key python application.py

```

* BEACON_HOST: The CNAME that points to b.siftscience.com.
* BEACON_KEY: The Sift Science Javascript Snippet Key


Replace the variable `my_beacon_key` with the appropriate key from the
[Sift Science Console](https://siftscience.com/console/developer/api-keys).

Then visit http://localhost:5000 to test.

