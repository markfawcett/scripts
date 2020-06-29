#!/usr/local/bin/python3

import sys


def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        file_string = f.read()

    file_string = file_string.replace(one, one_replace)
    file_string = file_string.replace(two, two_replace)

    output_file_name = input_file.rstrip('html') + 'htm'

    with open(output_file_name, 'w') as f:
        f.write(file_string)


one = '<!--#include virtual="/server-side/banner_pubs2010.htm"-->'
one_replace = """
            <div id="wrapper">
                <div id="header">
                    <a OnClick="window.location.href='http://www.parliament.uk/'" style="cursor:hand;cursor:pointer;"><img src="/assets/images/parliament-uk-logo.gif" alt="Parliament UK" /></a>
                    <form id="search-form" action="https://www.parliament.uk/search/results" method="get">
                        <fieldset class="site-search">
                            <ul>
                                <li><a href="https://www.parliament.uk/site-information/accessibility/">Accessibility</a></li>
                                <li><a href="https://www.parliament.uk/site-information/privacy/">Cookies</a></li>

                                <li><a href="https://www.parliament.uk/site-information/email-alerts/">Email alerts</a></li>
                                <li><a href="https://www.parliament.uk/site-information/rss-feeds/">RSS feeds</a></li>
                                <li class="last"><a href="https://www.parliament.uk/site-information/contact-us/">Contact us</a></li>
                            </ul>
                            <h4 class="marker">Site search</h4>
                            <legend>Site search</legend>
                            <ol>
                                <li>
                                    <label for="q">Search</label>
                                    <input id="q" type="text" name="q" />
                                </li>
                            </ol>
                            <input type="submit" value="Search" />
                        </fieldset>
                    </form>
                    <h4 class="marker">Primary navigation</h4>
                    <div id="navigation">
                        <ul id="level-1">
                            <li><a href="https://www.parliament.uk/">Home</a></li>
                            <li class="over"><a href="https://www.parliament.uk/business/">Parliamentary business</a></li>
                            <li><a href="https://www.parliament.uk/mps-lords-and-offices/">MPs, Lords &amp; offices</a></li>
                            <li><a href="https://www.parliament.uk/about/">About Parliament</a></li>
                            <li><a href="https://www.parliament.uk/get-involved/">Get involved</a></li>
                            <li><a href="https://www.parliament.uk/visiting/">Visiting</a></li>
                            <li class="last"><a href="https://www.parliament.uk/education/">Education</a></li>
                        </ul>
                        <ul id="level-2">
                            <li><a href="https://www.parliament.uk/business/commons/">House of Commons</a></li>
                            <li><a href="https://www.parliament.uk/business/lords/">House of Lords</a></li>
                            <li><a href="http://calendar.parliament.uk/">What's on</a></li>
                            <li><a href="https://www.parliament.uk/business/bills-and-legislation/">Bills &amp; legislation</a></li>
                            <li><a href="https://www.parliament.uk/business/committees/">Committees</a></li>
                            <li class="first over"><a href="https://www.parliament.uk/business/publications/">Publications &amp; records</a></li>
                            <li><a href="http://www.parliamentlive.tv/Commons">Parliament TV</a></li>
                            <li><a href="https://www.parliament.uk/business/news/">News</a></li>
                            <li><a href="https://www.parliament.uk/topics/topical-issues.htm">Topics</a></li>

                        </ul>
                    </div>
<div><p></p></div>
                </div>
<!-- URL not found - breadcrumb trail can't be generated -->"""

two = '<!--#include virtual="/server-side/footer2010.htm"-->'

# ! without Javascript
two_replace = """

                <div id="footer">
                    <h4 class="marker">Footer links</h4>
                    <ul>
                        <li><a href="https://www.parliament.uk/site-information/azindex/">A-Z index</a></li>
                        <li><a href="https://www.parliament.uk/site-information/glossary/">Glossary</a></li>
                        <li><a href="https://www.parliament.uk/site-information/contact-us/">Contact us</a></li>
                        <li><a href="https://www.parliament.uk/site-information/foi/">Freedom of Information</a></li>
                        <li><a href="https://www.parliament.uk/about/working/jobs/">Jobs</a></li>
                        <li><a href="https://www.parliament.uk/site-information/using-this-website/">Using this website</a></li>
                        <li class="last"><a href="https://www.parliament.uk/site-information/copyright/">Copyright</a></li>
                    </ul>
                </div>
            </div>

"""


if __name__ == "__main__":
    main()