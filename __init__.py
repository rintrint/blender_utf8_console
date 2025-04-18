bl_info = {
    "name": "控制台UTF8编码修复工具", 
    "description": "启动Blender时自动将Console控制台设置为UTF-8编码，解决中文显示乱码问题",
    "author": "rint",
    "version": (1, 0, 0),
    "blender": (2, 0, 0),
    "location": "自动运行，无界面操作",
    "category": "System",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY"
}

import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    """开启Blender时自动执行"""
    import os
    os.system("chcp 65001 > nul")

def register():
    bpy.app.handlers.load_post.append(load_handler)

def unregister():
    bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
    register()
