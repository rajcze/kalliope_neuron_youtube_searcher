# Latest video from youtube channel

## Synopsis

This neuron gives you a latest video title from channel you ask for

## Installation
```bash
kalliope install --git-url https://github.com/kalliope_neuron_youtube_searcher.git
```

## Options


| parameter choices | required |  comments          |   |   |
|-------------------|----------|--------------------|---|---|
| channel           | yes      | Name of YT channel |   |   |


## Return Values


| name      | description                        | type       | sample                    |
|-----------|------------------------------------|------------|---------------------------|
| title     | Title of latest YT video           | string     | "Démo Kalliopé FR"        |


## Synapses example

Description of what the synapse will do
```yml
 - name: "latest-video"
   signals:
     - order: "What's the latest video by {{ channel }}"
   neurons:      
     - youtube_searcher:
        channel: "{{ channel }}"
        file_template: templates/youtube_searcher.j2
    
```

## Templates example 

Description of the template
```
{% if returncode == "Nochannelfound" %}
    There is no such channel
{% elif returncode == "Novideofound" %}
    I couldn't find any video
{% elif returncode == "Notitlefound" %}
    I couldn't find requested title
{% else %}
    {{ title }}
{% endif %}
```