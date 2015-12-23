dir_name = '/root/Mormann data/031/031e01mv1-2014-06-04_14-49-06/'
channel_name = {}
for i =1:80;
    channel_name{i} = strcat('DS_Data',num2str(i),'.mat');
end

channels = []
for i=1:length(channel_name);
    data = load(strcat(dir_name,char(channel_name(i))));
    chan = data.DS_Data;
    channels = vertcat(channels,chan);
end
clear data
clear chan
