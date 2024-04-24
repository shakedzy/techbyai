require 'nokogiri'

module Jekyll
  module H1Filter
    def extract_h1_list(input)
      doc = Nokogiri::HTML(input)
      h1_tags = doc.css('h1')
      list_items = h1_tags.map { |h1| "- #{h1.content.strip}" }
      puts "Debug: Extracted H1 Tags - #{list_items}"  # Output extracted data
      list_items.join("\n")
    end
  end
end

Liquid::Template.register_filter(Jekyll::H1Filter)
