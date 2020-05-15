# Haiku-TTP-Codes

Haiku Messages for each HTTP Status Code

## source

[Wikipedia Article](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

## what the hell

A Slack conversation from an especially mean friend who doesn't respect my time resulted in a link to [Haiku Error Codes](https://www.gnu.org/fun/jokes/error-haiku.en.html).

I couldn't resist.


## i have opinions

Cool beans -- Submit a PR.  The skeleton of the JSON is setup for anyone to add another haiku
for each status code

### what do i do

See the top 9 status codes for examples:
1. [200 OK](./codes/official/2XX/200.json)
2. [201 Created](./codes/official/2XX/201.json)
3. [204 No Content](./codes/official/2XX/204.json)
4. [400 Bad Request](./codes/official/4XX/400.json)
5. [401 Unauthorized](./codes/official/4XX/401.json)
6. [403 Forbidden](./codes/official/4XX/403.json)
7. [404 Not Found](./codes/official/4XX/404.json)
8. [409 Conflict](./codes/official/4XX/409.json)
9. [500 Internal Server Error](./codes/official/5XX/500.json)

### what's missing

Use the `tools/entries.py` file to Find data about what needs work.

**Requires [rich](https://github.com/willmcgugan/rich) to run** -- (`pip install rich`)

`./entries.py` lists all codes and their haiku count

`./entries.py empty` lists only codes that have no haikus yet

## whiny standards

Let's try to have each entry in the `"messages"` list be of the format
```
"FIRST_LINE_OF_HAIKU // SECOND_LINE_OF_THE_HAIKU // LAST_LINE_OF_HAIKU"
```

This will make it stupid simple for people to parse in any language that has sane string splitting.

### what if i want a `//` in my haiku text

Guess whose PR ain't gettin' merged then?

### i don't like the structure

`(•_•)   ( •_•)>⌐■-■   (⌐■_■)`

### <word> doesn't have <num> syllables

[Yes](https://www.howmanysyllables.com/) [It](http://www.syllablecount.com/) [Does](https://www.poetrysoup.com/)

## i need this in my project

I am so sorry for your users, but okay.  I would love to have supported packages for each language to be deployed to various package managers.

Submit a PR to add support for yours if you want!  I don't plan to do them myself, that should be for smarter people.
