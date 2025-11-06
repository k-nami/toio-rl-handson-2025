import asyncio

from toio import *


async def move2pos(cube_id):
    """PositionIDへ移動"""
    assert cube_id != "", "cube_idを入力してください"

    # 接続
    dev_list = await BLEScanner.scan_with_id(cube_id={cube_id})
    assert len(dev_list)
    cube = ToioCoreCube(dev_list[0].interface, name=dev_list[0].name)
    await cube.connect()

    # 位置を表示
    def id_notification_handler(payload: bytearray):
        id_info = IdInformation.is_my_data(payload)
        if isinstance(id_info, PositionId):
            print(f"{id_info.center=}")

    # 登録
    await cube.api.id_information.register_notification_handler(id_notification_handler)

    await asyncio.sleep(4)

    #TODO: PositionID(200,200)へ移動

    await asyncio.sleep(4)

    # 接続解除
    await cube.disconnect()
    return 0


#TODO: 呼び出し元
