def markdown_to_blocks(markdown):
   final_block_list = []
   block_list = markdown.split("\n\n")
   for block in block_list:
       block = block.strip()
       if len(block) == 0:
           continue
       else:
           final_block_list.append(block)
   return final_block_list
