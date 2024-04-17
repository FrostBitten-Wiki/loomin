## Copied from the old janky backend. will be remade to a better one.

class PostProcessors:
    @staticmethod
    def section(match):
        level = len(match.group(1))
        title = match.group(2)

        fontSize = {1: "35px", 2: "25px", 3: "20px"}.get(level, "25px")
        sep = ""
        if level != 3: sep = "<div style=\"width: 100%; height: 1px; background-color: white; margin-top: 2px; margin-bottom: 5px; box-shadow: 0 2px 0 #000000;\"></div>"
        
        return f"""
<div style="margin-top: 20px;" id="{title.lower().replace(" ", "-")}">
    <text style="font-size: {fontSize};">{title}</text>
    {sep}
</div>
"""
    
    @staticmethod
    def quote(match):
        quote = match.group(1)
        author = match.group(2)

        return f"""
<div style="margin-top: 20px; margin-bottom: 30px">
    <div style="display: grid; grid-template-columns: 0.05fr 1fr 0.05fr;">
        <text style="font-size: 50px;">"</text>
        <text style="text-align: center;">{quote}</text>
        <text style="font-size: 50px; text-align: right;">"</text>
    </div><br>
    <text>- {author}</text>
</div>
"""
    
    @staticmethod
    def dialogueEmulator(match):
        emulatorId = match.group(1)
        startId = match.group(2)
        datasetURL = match.group(3)

        return f"""
<div style="margin-top: 20px; margin-bottom: 30px">
    <div id="{emulatorId}-dialogue" class="checkBg" style="margin-bottom: 5px; padding: 10px; --color1: grey; --color2: white; --color3: grey; width: calc(100% - 28px); height: 150px;" onclick="window.{emulatorId}dialogueDelay = 5">
        <text id="{emulatorId}-name" style="font-size: 20px;"></text><br>
        <text id="{emulatorId}-chat"></text>
    </div>

    <text id="{emulatorId}-note" style="margin-top: 5px; margin-bottom: 10px;"></text>

    <div id="{emulatorId}-choices" style="padding: 0; gap: 0 5px;  display: flex; justify-content: space-between; align-items: center;">
    </div>

    <div id="{emulatorId}-controls" style="padding: 0; gap: 0 5px;  display: flex; justify-content: space-between; align-items: center;">
    </div>

    <script defer>
        var {emulatorId}chatDataset;
        var {emulatorId}dialogueDelay = 25;

        fetch("{datasetURL}")
        .then(response => response.json())
        .then(data => {{
            console.log(data);
            {emulatorId}chatDataset = data;
            console.log("dataset append -> {emulatorId}");
            changeDialogue("{emulatorId}", "{startId}");
        }})
        .catch(error => console.error('Emulator Dataset failed to Load: ', error));

    </script>
<div>
"""

    @staticmethod
    def gallery(match):
        urls = match.group(1).split("|")
        imageList = ""

        for image in urls:
            imageList += f'        <img src="{image}" style="cursor: pointer;" onclick="previewImage(this)" alt="Open Image" loading="lazy">\n'

        return f"""
<div style="margin-top: 20px; margin-bottom: 30px" id="gallery">
    <text style="font-size: 25px;">Gallery</text>
    <div class="gallery-container" style="margin-bottom: 20px;">
        <div class="gallery" style="padding: 10px;">
    {imageList}
        </div>
    </div>
</div>
"""
        
    @staticmethod
    def listItem(match):
        image = match.group(1)
        title = match.group(2)
        desc = match.group(3)
        redir = match.group(4)

        if redir == "":
            if image == "":
                return f"""
<div class="container" style="padding: 10px;">
    <text style="font-size: 25px;">{title}</text><br>
    <text>{desc}</text>
</div>
"""
            else:
                return f"""
<div class="container" style="padding: 10px; display: grid; grid-template-columns: 128px 1fr; gap: 10px;">
    <img src="{image}" height="128" width="128" style="object-fit: cover;" loading="lazy">

    <div>
        <text style="font-size: 25px;">{title}</text><br>
        <text>{desc}</text>
    </div>
</div>
"""
        else:
            if redir.startswith("/wiki"):
                redir = f"{redir}"
            else:
                redir = f"/wiki{redir}"
            
            if image == "":
                return f"""
<div class="container" style="padding: 10px; cursor: pointer;" onclick="renderHTML(`{redir}`)">
    <text style="font-size: 25px;">{title}</text><br>
    <text>{desc}</text>
</div>
"""
            else:
                return f"""
<div class="container" style="padding: 10px; cursor: pointer; display: grid; grid-template-columns: 128px 1fr; gap: 10px;" onclick="renderHTML(`{redir}`)">
    <img src="{image}" height="128" width="128" style="object-fit: cover;" loading="lazy">

    <div>
        <text style="font-size: 25px;">{title}</text><br>
        <text>{desc}</text>
    </div>
</div>
"""
    
    @staticmethod
    def buttons(match):
        buttons = match.group(1).split("|")
        
        buttonList = ""
        for button in buttons:
            button = button.split(",")
            buttonList += f"""
<button style="flex: auto;" onclick="{button[1]}">
    <text type="hoverText">{button[0]}</text>
</button>\n
"""
        
        return f"""
<div style="margin-top: 20px; margin-bottom: 30px">
    <div style="padding: 0; gap: 0 5px;  display: flex; justify-content: space-between; align-items: center;">
        {buttonList}
    </div>
</div>
"""

    @staticmethod
    def infobox(match):
        title = match.group(1)
        color = match.group(2)
        text = match.group(3).replace("\"", "&quot;")

        return f"""
<div style="margin-top: 20px; padding: 10px;" class="container">
    <text style="color: {color}; font-size: 25px;">{title}</text><br>
    <text>{text}</text>
</div>
"""

    @staticmethod
    def link(match):
        text = match.group(1)
        url = match.group(2)
        if not url.startswith("https://"):
            if url.startswith("/wiki"):
                return f'<a onclick="renderHTML(\'{url}\');">{text}</a>'
            else:
                return f'<a onclick="renderHTML(\'/wiki{url}\');">{text}</a>'
        else:
            return f'<a href="{url}">{text}</a>'

    @staticmethod
    def image(match):
        width, height = match.group(1).split("x")
        image = match.group(2)

        return f'<img src="{image}" width="{width}" height="{height}">'
