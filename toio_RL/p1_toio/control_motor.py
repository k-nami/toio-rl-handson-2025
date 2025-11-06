import asyncio

from toio import *


async def control_motor(cube_id):
    """モーターのスピードを指定して操作"""
    assert cube_id != "", "cube_idを入力してください"

    # 接続
    dev_list = await BLEScanner.scan_with_id(cube_id={cube_id})
    assert len(dev_list)
    cube = ToioCoreCube(dev_list[0].interface, name=dev_list[0].name)
    await cube.connect()

    #TODO: 2秒回転, モーターごとに速度指定

    # 接続解除
    await cube.disconnect()
    return 0


#TODO: 呼び出し元
