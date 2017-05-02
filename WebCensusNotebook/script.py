# initialization
%matplotlib inline
import sys, os
sys.path.append(os.path.realpath('censuslib'))
from censuslib import census
cen = census.Census('census_2016_10_1m_stateless')

# sample data
l1 = [('doubleclick.net','208'), ('google-analytics.com','204'), ('google.com','171'), ('facebook.com','164'), ('facebook.net','152'), ('fonts.googleapis.com','110'), ('googleadservices.com','104'), ('rlcdn.com','87'), ('googletagmanager.com','85'), ('twitter.com','83'), ('ajax.googleapis.com','76'), ('liadm.com','74'), ('adnxs.com','71'), ('pinterest.com','68'), ('bing.com','66'), ('gstatic.com','64'), ('criteo.com','64'), ('yahoo.com','61'), ('rubiconproject.com','59'), ('demdex.net','57'), ('nr-data.net','54'), ('newrelic.com','54'), ('scorecardresearch.com','51'), ('casalemedia.com','49'), ('openx.net','48'), ('youtube.com','47'), ('mathtag.com','46'), ('criteo.net','46'), ('akamaihd.net','44'), ('pinimg.com','44')]
l1_org = [('Google','260'), ('Facebook','171'), ('Acxiom','94'), ('Twitter','83'), ('Adobe','81'), ('Microsoft','75'), ('LiveIntent','74'), ('AppNexus','71'), ('Criteo','70'), ('Yahoo','69')]
l2 = [('doubleclick.net','104'), ('mathtag.com','89'), ('liadm.com','74'), ('bluekai.com','68'), ('bidswitch.net','67'), ('licasd.com','65'), ('voicefive.com','64'), ('adnxs.com','57'), ('mojn.com','57'), ('advertising.com','52'), ('wtp101.com','49'), ('adsrvr.org','47'), ('w55c.net','47'), ('exe.bid','46'), ('creative-serving.com','46'), ('tapad.com','45'), ('rlcdn.com','45'), ('bilinmedia.net','44'), ('sitescout.com','44'), ('company-target.com','42'), ('demdex.net','40'), ('2mdn.net','40'), ('adsymptotic.com','39'), ('nexac.com','38'), ('dotomi.com','35')]
l3 = [('doubleclick.net','202'), ('google-analytics.com','196'), ('google.com','158'), ('facebook.net','152'), ('facebook.com','145'), ('fonts.googleapis.com','110'), ('googleadservices.com','103'), ('googletagmanager.com','85'), ('twitter.com','79'), ('ajax.googleapis.com','76'), ('adnxs.com','71'), ('bing.com','66'), ('gstatic.com','64'), ('pinterest.com','58'), ('rubiconproject.com','56'), ('demdex.net','55'), ('yahoo.com','55'), ('rlcdn.com','54'), ('newrelic.com','54'), ('nr-data.net','53'), ('criteo.com','53'), ('openx.net','48'), ('casalemedia.com','48'), ('youtube.com','47'), ('criteo.net','46')]
l3_org = [('Google','251'), ('Facebook','163'), ('Twitter','79'), ('Adobe','78'), ('Microsoft','74'), ('AppNexus','71'), ('Yahoo','67'), ('Akamai','66'), ('Pinterest','66'), ('Criteo','59')]
l4 = [('google-analytics.com','164'), ('doubleclick.net','132'), ('facebook.com','127'), ('google.com','104'), ('bing.com','56'), ('pinterest.com','50'), ('liadm.com','50'), ('twitter.com','40'), ('scorecardresearch.com','37'), ('quantserve.com','33'), ('omtrdc.net','29'), ('instagram.com','28'), ('dotomi.com','27'), ('mpstat.us','25'), ('demdex.net','23'), ('yahoo.com','22'), ('youtube.com','22'), ('criteo.com','21'), ('monetate.net','20'), ('maps.googleapis.com','19'), ('googleadservices.com','18'), ('optimizely.com','17'), ('triggeredmail.appspot.com','17'), ('res-x.com','16'), ('brsrvr.com','16')]
l4_org = [('Google','185'), ('Facebook','127'), ('Microsoft','58'), ('LiveIntent','50'), ('Pinterest','50'), ('Twitter','40'), ('Adobe','38'), ('comScore','37'), ('Quantcast','33'), ('Conversant Media','27')]
l5 = [('liadm.com','68'), ('google-analytics.com','41'), ('rlcdn.com','40'), ('pippio.com','37'), ('doubleclick.net','35'), ('facebook.com','33'), ('acxiom-online.com','31'), ('dotomi.com','25'), ('google.com','23'), ('bluekai.com','21'), ('scorecardresearch.com','18'), ('quantserve.com','17'), ('pinterest.com','16'), ('twitter.com','15'), ('criteo.com','14'), ('thebrighttag.com','14'), ('bing.com','14'), ('rubiconproject.com','13'), ('instagram.com','10'), ('adnxs.com','10'), ('yahoo.com','9'), ('gigya.com','8'), ('googlesyndication.com','8'), ('adsafeprotected.com','8'), ('optimizely.com','7')]
l5_org = [('LiveIntent','68'), ('Acxiom','48'), ('Google','47'), ('Facebook','33'), ('Conversant Media','25'), ('Oracle','22'), ('comScore','18'), ('Quantcast','17'), ('Pinterest','16'), ('Microsoft','15')]

# print census info by third party
total_fp = float(len(cen.first_parties))
for site, count in l1:
    try:
        org = cen.third_parties[site].organization.name
    except:
        org = ''
    try:
        pct = len(cen.third_parties[site].first_parties) / total_fp * 100.
    except:
        pct = 0
    print(site + ',' + org + ',' + count + ',' + str(pct))

# print census info by organization
total_fp = float(len(cen.first_parties))
for org_name, count in l1_org:
    first_parties_with_org = set()
    try:
        for domain in cen.organizations[org_name].domains:
            try:
                first_parties_with_org.update(cen.third_parties[domain].first_parties)
            except:
                continue
    except:
        pass
    try:
        pct = len(first_parties_with_org) / total_fp * 100.
    except:
        pct = 0
    print(org_name + ',' + count + ',' + str(pct))
