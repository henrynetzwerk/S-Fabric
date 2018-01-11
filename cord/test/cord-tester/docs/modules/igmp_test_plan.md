**Cord-Tester**



**CORD Automated Tester Suite:**

**The CORD Automated Tester Suite (CATS) is an extensible end-to-end system test suite targeting CORD PODs. It is typically deployed as one or more Docker containers, either on the CORD POD or adjacent to the POD and interacts with the POD through the PODs interfaces.**

**Its intended use includes:**

**● Functional Testing**

**● Regression testing for CORD related component development**

**● Acceptance testing of a deployed CORD POD**

**● Health-testing of an existing CORD POD (including non-service-impacting and possibly service-impacting tests)**

**IGMP Test Cases (Implemented and Planned) : **

<table>
  <tr>
    <td>ID</td>
    <td>Title</td>
    <td>Function Name</td>
    <td>Test Steps</td>
    <td>Expected Result</td>
    <td>Actual Result</td>
  </tr>
  <tr>
    <td>IGMP_1</td>
    <td>Verify the traffic flow after joining </td>
    <td>test_igmp_join_verify_traffic</td>
    <td>1. Send a IGMP join message to a particular group from an interface
2. Check for traffic flow </td>
    <td>Traffic should get received on that interface</td>
    <td>
Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_2</td>
    <td>Verify the traffic after leaving from the group</td>
    <td>test_igmp_leave_verify_traffic</td>
    <td>1. Leave a group from an interface.
2. Check for traffic flow</td>
    <td>Traffic should not get received on that interface</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_3</td>
    <td>Verify joining loop</td>
    <td>test_igmp_leave_join_loop</td>
    <td>Send a join message to the groups in the same subnet</td>
    <td>Joining interface should receive traffic</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_4</td>
    <td>Check for latency with 1  group</td>
    <td>test_igmp_1group_join_latency</td>
    <td>1. Send a join message to one group from intf1.
2. Send multicast data from intf2.
3. Check for the latency of the data which is sent from intf2 to intf1</td>
    <td>Latency should be checked when the data is being received on intf1</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_5</td>
    <td>Check for latency with 2 groups</td>
    <td>test_igmp_2group_join_latency</td>
    <td>1. Send a join message to 2 groups from 2  different interfaces
2. Send multicast data to 2 groups.
3. Check for the latency of the data</td>
    <td>Latency should be checked when the data is being received on 2 different interfaces</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_6</td>
    <td>Check for latency with N groups</td>
    <td>test_igmp_Ngroup_join_latency</td>
    <td>1. Send a join message to N groups from N different interfaces
2. Send multicast data to N groups.
3. Check for the latency of the data</td>
    <td>Latency should be checked when the data is being received on N different interfaces</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_7</td>
    <td>Verify IGMP query packet</td>
    <td>test_igmp_query</td>
    <td>1. Send a Leave message to the group 224.0.0.1.
2. Check for IGMP query message from the router.</td>
    <td>ONOS should send the IGMP Query message to 224.0.0.1</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_8</td>
    <td>Verify leaving group2 when group1 is still alive</td>
    <td>test_igmp_2joins_1leave_functionality</td>
    <td>1. Send a join message to  group1 and check  the traffic.
2. Send a leave message to group2  and check the traffic on the interface1</td>
    <td>1. Traffic should get received on an interface.
2. Traffic should  get received without any interruptions.</td>
    <td>Pass
 </td>
  </tr>
  <tr>
    <td>IGMP_9</td>
    <td>Verify rejoining to the same group</td>
    <td>test_igmp_2joins_1leave_again_joins_functionality</td>
    <td>1. Send a join message to 2 groups.
2. Send a leave message to group2 and join back again</td>
    <td>Traffic should get received on interface.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_10</td>
    <td>Verify joining a group with source ip as 0.0.0.0</td>
    <td>test_igmp_join_sourceip_0_0_0_0_functionality</td>
    <td>1. Send a join message to a group with source ip as 0.0.0.0
2. Check the traffic on the interface.</td>
    <td>Traffic should not get received.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_11</td>
    <td>Verify the traffic when invalid join message is being sent</td>
    <td> test_igmp_invalidClassD_IP_join_packet_functionality</td>
    <td>Send an invalid join message to a group. Eg class D IP</td>
    <td>Traffic should not get received.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_12</td>
    <td>Verify periodic general query messages</td>
    <td>test_igmp_periodic_query_packet_received_on_joining_interface</td>
    <td>Send a Join packet  to a particular group. </td>
    <td>Joining interface should receive multiple periodic general query packets from ONOS</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_13</td>
    <td>Verify general membership query packet</td>
    <td>test_igmp_query_packet_received_on_joining_interface</td>
    <td>Send a join message and wait for membership query packet</td>
    <td>General membership query packet should be received from querier router after 60sec</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_14</td>
    <td>Verify the traffic after 180sec</td>
    <td>test_igmp_general_query_recv_packet_traffic_functionality</td>
    <td>1. Let onos send query packets.
2. For 180 sec, hosts should not respond.
3. Check for multicast data.</td>
    <td>Multicast data should stop after 180 sec of time.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_15</td>
    <td>Verify the traffic after the interface is made down and then up.</td>
    <td>test_igmp_join_data_receiving_during_subscriber_link_up_down_functionality</td>
    <td>1. Send a join message to the group from the intf1
2. Bring down the intf1.
3. Make the intf1 up again.</td>
    <td>Traffic should get stopped and then resume once the interface is made up.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_16</td>
    <td>Check for "include" source list</td>
    <td>test_igmp_include_to_allow_src_list_functionality</td>
    <td>Send a join message with the include source list as A,B</td>
    <td>Traffic sent from any of the source address should not get filtered</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_17</td>
    <td>Check for “Exclude” source list</td>
    <td>test_igmp_exclude_to_allow_src_list_functionality</td>
    <td>Send a join message with the exclude source list as C</td>
    <td>Traffic sent from any of the source address should get filtered.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_18</td>
    <td>Changing filter to Include mode</td>
    <td>test_igmp_change_to_include_src_list_functionality</td>
    <td>1. Send a join message with Exclude mode.
2. Now change it to Include.</td>
    <td>Traffic sent from any of the source address should now not get filtered</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_19</td>
    <td>Changing filter to Exclude mode</td>
    <td>test_igmp_change_to_exclude_src_list_functionality</td>
    <td>1. Send join message with Include mode.
2. Now change it to Exclude. </td>
    <td>Traffic sent from any of the source address should now get filtered</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_20</td>
    <td>Verify Allowing new sources list</td>
    <td>test_igmp_new_src_list_functionality</td>
    <td>1. Send join message with include mode for A and B.
2. Add a new source list for C.
3. Check the traffic</td>
    <td>Traffic sent from the new source list should now not get filtered.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_21</td>
    <td>Verify Blocking Old sources list</td>
    <td>test_igmp_block_old_src_list_functionality</td>
    <td>1. Send join message with include mode for A and B.
2. Disallow A and B now.</td>
    <td>Traffic sent from the new source list should now be filtered.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_22</td>
    <td>Verify sending multicast data which is not in Join group</td>
    <td>test_igmp_not_in_src_list_functionality</td>
    <td>1. Let the join group has 2.2.2.2 and 3.3.3.3
2. Send a multicast data from 6.6.6.6</td>
    <td>The joining interfaces should not receive the multicast data.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_23</td>
    <td>Verify the traffic when invalid join message is being sent with source list</td>
    <td>test_igmp_invalid_join_packet_functionality</td>
    <td>1. Send a join message with the include source list as A,B
2. Specify the source ip be as 255.255.255.255</td>
    <td>Traffic should not get received.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_24</td>
    <td>Verify general query packet for Include(A) and Allow(B)</td>
    <td>test_igmp_include_to_allow_src_list_check_for_general_query</td>
    <td>1. Send a join message with include mode for A and Allow for B.
2. Check for membership query packet</td>
    <td>General membership query packet should get received from both A and B source list.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_25</td>
    <td>Verify specific query packet for Include(A) and Block(B)</td>
    <td>test_igmp_include_to_block_src_list_check_for_group_source_specific_query</td>
    <td>1. Send a join message with include mode with source list A for G1 and Allow with new source list B for G1.
2. Check for specific query packet</td>
    <td>Source  membership query packet should get received to A*B source list interface</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_26</td>
    <td>Verify general query packet for Exclude(A) and Allow(B)</td>
    <td>test_igmp_exclude_to_allow_src_list_check_for_general_query</td>
    <td>1. Send a join message Exclude mode with source list A for G1 and Allow with new source list B for G1.
2. Check for general membership query packet</td>
    <td>General membership query packet should get received on A*B source list interface</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_27</td>
    <td>Verify query packet for Exclude(A) and Block(B)</td>
    <td>test_igmp_exclude_to_block_src_list_check_for_group_source_specific_query(</td>
    <td>1. Send a join message with  Exclude mode with source list A for G1 and block with new source list B for G1.
2. Check for Specific query packet</td>
    <td>Specific query packet should not get received.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_28</td>
    <td>Verify traffic for INCLUDE (A) and Block(B)</td>
    <td>test_igmp_include_to_block_src_list_functionality</td>
    <td>1. Send a join message with Include mode for A and Block for B.
2. Check for multicast traffic</td>
    <td>Multicast traffic should get received from  A source list.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_29</td>
    <td>Verify joining across multicast range of address </td>
    <td>test_igmp_join_rover</td>
    <td>Keep sending joins across different multicast range of address. </td>
    <td>Joining interface should receive traffic for all the groups.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_30</td>
    <td>Verify empty source list include</td>
    <td>test_igmp_include_empty_src_list_functionality</td>
    <td>Send a join message with include mode with empty source list</td>
    <td>It should be unsuccessful</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_31</td>
    <td>Verify empty source list Exclude</td>
    <td>test_igmp_exclude_empty_src_list_functionality</td>
    <td>Send a join message with Exclude mode with empty source list</td>
    <td>It should be unsuccessful</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_32</td>
    <td>Verify invalid Class D ip join packet with source list</td>
    <td>test_igmp_invalidClassD_IP_as_srclistIP_join_packet_functionality</td>
    <td>1. Send a join message with the include source list as A,B
2. Specify the source ip be as 239.5.5.5</td>
    <td>Traffic shouldn't get received</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_33</td>
    <td>Verify the traffic after the channel is made down and then up.</td>
    <td> test_igmp_join_data_receiving_during_channel_distributor_link_down_up_functionality</td>
    <td>1. Send a join message to the group from the intf1
2. Bring down the channel
4. Make the channel up again.</td>
    <td>Traffic should get stopped and then resume.</td>
    <td>To Be implemented</td>
  </tr>
  <tr>
    <td>IGMP_34</td>
    <td>Verify entry deletion after membership query time expires</td>
    <td>test_igmp_periodic_query_packet_received_and_checking_entry_deleted</td>
    <td>Send IGMP join and wait till 3 membership query packets are received. Check for traffic</td>
    <td>Traffic shouldn't get received.
ONOS should not show the entry for MF table </td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_35</td>
    <td>Verify rejoining interface after membership query interval expires</td>
    <td>test_igmp_member_query_interval_expire_re_joining_interface</td>
    <td>1.Send IGMP join and wait till 3 membership query packets are received.
2. After the timer expires, again rejoin the interface</td>
    <td>Rejoining the interface should happen and traffic flow should be seen.</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_36</td>
    <td>Verify source specific query for leave message</td>
    <td>test_igmp_leave_verify_received_group_source_specific_query</td>
    <td>1.Leave a group from an interface.
2.Check for source specific query</td>
    <td>Source specific query should not get received on that interface</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_37</td>
    <td>Verify group specific query packet after changing to exclude mode</td>
    <td>test_igmp_change_to_exclude_src_list_check_for_group_source_specific_query</td>
    <td>1. Send join message with Include mode.
2. Now change it to Exclude.
3. Check for specific query packet</td>
    <td>Specific query packet  sent from any of the source address should now get filtered</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_38</td>
    <td>Verify group specific query packet after changing to Include mode</td>
    <td>test_igmp_change_to_include_src_list_check_for_general_query</td>
    <td>1. Send a join message with Exclude mode.
2. Now change it to Include.
3. Check for General query packet</td>
    <td>General query packet  sent from any of the source address should not get filtered</td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_39</td>
    <td>Verify igmp include and exclude modes </td>
    <td>test_igmp_include_exclude_modes</td>
    <td>send igmp join for include mode
Send igmp join for exclude mode
Send traffic to both the groups</td>
    <td>Traffic should receive for include mode group only</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_40</td>
    <td>Verify igmp allow new source mode </td>
    <td>test_igmp_allow_new_source_mode</td>
    <td>Send igmp include mode join
Send traffic
Send allow new source to the same group
Send traffic with newly allowed source </td>
    <td>Traffic should receive with newly allowed source </td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_41</td>
    <td>Verify igmp include mode to exclude mode change</td>
    <td>test_igmp_include_to_exclude_mode_change</td>
    <td>send igmp include mode join
Send traffic to above group
Send exclude mode join to same group
Send traffic now</td>
    <td>Traffic should receive when join sent as include mode and traffic should not receive  when exclude mode sent</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_42</td>
    <td>Verify igmp exclude mode to include mode change</td>
    <td>test_igmp_exclude_to_include_mode_change</td>
    <td>1.send igmp exclude mode join
2.Send traffic to above group
3.Send include mode join to same group
4. Send traffic now</td>
    <td>Traffic should receive when join sent as include mode and traffic should not receive  when exclude mode sent</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_43</td>
    <td>Verify igmp to_include with null source list </td>
    <td>test_igmp_to_include_mode_with_null_source</td>
    <td>Send igmp include ode join
Send traffic
Send to_include mode with empty source join to same group</td>
    <td>After sending to_include with empty source list, traffic should not receive </td>
    <td>Need to test on multicast router connected setup</td>
  </tr>
  <tr>
    <td>IGMP_44</td>
    <td>Verify igmp to_include mode </td>
    <td>test_igmp_to_include_mode</td>
    <td>send igmp include mode join
Send traffic
Send igmp to_include to same group with other source
Send traffic </td>
    <td>Traffic should receive when traffic sent from other sources also</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>
IGMP_45</td>
    <td>Verify igmp block old source mode </td>
    <td>test_igmp_blocking_old_source_mode</td>
    <td>send igmp join with include mode
Send traffic
Send join with block old sources
Send traffic with source blocked </td>
    <td>Traffic should not receive once the source has blocked </td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_46</td>
    <td>Verify igmp traffic for 100 groups </td>
    <td>test_igmp_multiple_joins_and_data_verification_with_100_groups</td>
    <td>send 100 igmp joins
Send traffic to all 100 groups </td>
    <td>Traffic should receive for all 100 groups</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_47</td>
    <td>Verify igmp-leave</td>
    <td>test_igmp_multiple_joins_with_data_verification_and_leaving_100_groups</td>
    <td>send 100 igmp joins
Send traffic to each group
Send leave to each group</td>
    <td>Traffic should not received once the group receives leave </td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_48</td>
    <td>
Verify onos stability when ssm table filled with 1000 entries </td>
    <td>test_igmp_group_source_for_only_config_with_1000_entries</td>
    <td>Push igmp ssm entries for 1000 groups into onos </td>
    <td>Verify if all groups lists  in ‘netcfg’ command in onos and onos should be stable </td>
    <td>Need to check for max entries support in ONOS ssm table </td>
  </tr>
  <tr>
    <td>IGMP_49</td>
    <td>Verify exclue to include mode for 100 groups</td>
    <td>test_igmp_from_exclude_to_include_mode_with_100_groups</td>
    <td>send igmp join exclude mode
Send traffic
Send igmp join to include mode
Send traffic
Repeat steps for 100 groups</td>
    <td>Traffic should receive in case of include sent</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_50</td>
    <td>Verify igmp include mode traffic for 1000 groups</td>
    <td>test_igmp_with_multiple_joins_and_data_verify_with_1000_groups</td>
    <td>send igmp join with include mode
Send traffic to above join
Repeat for 1000 groups</td>
    <td>Traffic should receive for all 1000 groups</td>
    <td>Pass
</td>
  </tr>
  <tr>
    <td>IGMP_51</td>
    <td>Verify igmp include mode traffic for 5000 groups</td>
    <td>test_igmp_with_multiple_joins_and_data_verify_with_5000_groups</td>
    <td>1.send igmp join with include mode
2.Send traffic to above join
3. Repeat for 5000 groups
</td>
    <td>Traffic should receive for all 5000 groups</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_52</td>
    <td>Verify sending traffic to not registered igmp group</td>
    <td>test_igmp_send_data_to_non_registered_group</td>
    <td>send igmp join include mode for group G1
Send data traffic to group G2</td>
    <td>Traffic to G2 should not received on client side</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_53</td>
    <td>Verify igmp data traffic without sending join </td>
    <td>test_igmp_traffic_verification_for_registered_group_with_no_join_sent</td>
    <td>Dont send igmp join for group G1
Send data traffic to group G1</td>
    <td>As the join not registered data traffic should not received on any interface </td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_54</td>
    <td>Verify igmp functionality with app deactivation </td>
    <td>test_igmp_toggling_app_activation</td>
    <td>send igmp join include mode
Send data traffic to above group
Deactivate igmp app
Repeat step 2</td>
    <td>After app deactivate data traffic should not receive on any interface</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_55</td>
    <td>Verify igmp traffic sent to mismatching destination ip and mac</td>
    <td>test_igmp_with_mismatch_for_dst_ip_and_mac_in_data_packets</td>
    <td>send igmp include mode join
Send data traffic
Data traffic again with dest mac and IP addresses mismatch </td>
    <td>Incase of dest mac and IP mismatch, client should not receive traffic </td>
    <td>Fail</td>
  </tr>
  <tr>
    <td>IGMP_56</td>
    <td>Verify ig igmp module registers invalid IP address</td>
    <td>test_igmp_registering_invalid_group</td>
    <td>send igmp join include mode for valid multicast ip
Repeat step for invalid IP </td>
    <td>Joins sent to invalid multicast IPs should not get registered</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>IGMP_57</td>
    <td>Verify igmp join sent with invalid source IP should not register </td>
    <td>test_igmp_registering_invalid_source</td>
    <td>1.send igmp include mode join with invalid source IP</td>
    <td>Join should not get registered </td>
    <td>Pass</td>
  </tr>
</table>
