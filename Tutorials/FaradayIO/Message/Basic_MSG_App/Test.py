import faraday_msg
faraday_tx_msg_sm = faraday_msg.Msg_State_Machine_Tx()
faraday_tx_msg_object = faraday_msg.message_app_Tx()
faraday_rx_msg_object = faraday_msg.message_app_Rx()

faraday_tx_msg_object.UpdateDestinationStation('KB1LQC', 1)
message = 'This is a test of very long messages that should be longer than a single packet!'
faraday_tx_msg_sm.CreateMsgPackets('kb1lqd', 7, message)

for i in range(0, len(faraday_tx_msg_sm.list_packets), 1):
    faraday_tx_msg_object.TransmitFrame(faraday_tx_msg_sm.list_packets[i])
    #print repr(faraday_tx_msg_sm.list_packets[i])
