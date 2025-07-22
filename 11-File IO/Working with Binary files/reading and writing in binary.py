with open("Screenshot3.png","rb") as f:
    with open("screenshot_copy.png","wb") as wf:
        wf.write(f.read())