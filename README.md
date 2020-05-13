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


## whiny standards

Let's try to have each entry in the `"messages"` list be of the format
```json
{
    ...,
    "messages": [
        ...,
        "FIRST_LINE_OF_HAIKU // SECOND_LINE_OF_HAIKU // LAST LINE OF HAIKU"
    ]
}
```

This will make it stupid simple for people to parse in any language that has sane string splitting.

### what if i want a `//` in my haiku text

Guess whose PR ain't gettin' merged then?

### i don't like the structure

`(•_•)   ( •_•)>⌐■-■   (⌐■_■)`

## i need this in my project

I am so sorry for your users, but okay.  I would love to have supported packages for each language to be deployed to various package managers.

Submit a PR to add support for yours if you want!  I don't plan to do them myself, that should be for smarter people.